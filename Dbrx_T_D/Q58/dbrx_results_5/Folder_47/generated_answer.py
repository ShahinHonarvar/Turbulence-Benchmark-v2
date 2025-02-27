import numpy as np

def submatrix_with_n_numbers(matrix):
    N = 90
    n_rows, n_cols = matrix.shape
    result = 0
    for i in range(n_rows - N + 1):
        for j in range(n_cols - N + 1):
            submatrix = matrix[i:i + N, j:j + N]
            if submatrix.size == N * N and submatrix.sum() == n_numbers:
                result += 1
    return result