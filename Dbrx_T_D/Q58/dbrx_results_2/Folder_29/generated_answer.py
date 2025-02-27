import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 19
    rows, cols = matrix.shape
    submatrix_count = 0
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.sum(submatrix) == n * n:
                submatrix_count += 1
    return submatrix_count