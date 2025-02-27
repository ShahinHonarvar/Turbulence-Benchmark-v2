import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 23
    submatrix_count = 0
    rows, cols = matrix.shape
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.size(submatrix) == n ** 2:
                submatrix_count += 1
    return submatrix_count