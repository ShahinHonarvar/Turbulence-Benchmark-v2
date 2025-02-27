import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 24
    rows, cols = matrix.shape
    num_submatrices = 0
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.sum(submatrix) == n * n * (n * n - 1) // 2:
                num_submatrices += 1
    return num_submatrices