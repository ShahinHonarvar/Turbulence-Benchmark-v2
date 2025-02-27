import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 77
    rows, cols = matrix.shape
    submatrix_count = 0
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            if np.sum(matrix[i:i + n, j:j + n]) == n * n:
                submatrix_count += 1
    return submatrix_count