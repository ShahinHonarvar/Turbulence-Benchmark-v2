import numpy as np

def submatrix_with_n_numbers(matrix):
    row, col = matrix.shape
    submatrix_count = 0
    n = 173
    for i in range(row - n + 1):
        for j in range(col - n + 1):
            if np.sum(matrix[i:i + n, j:j + n]) == n * n:
                submatrix_count += 1
    return submatrix_count