import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    n = 60
    m, n_rows, n_cols = matrix.shape
    for i in range(n_rows - n + 1):
        for j in range(n_cols - n + 1):
            submatrix = matrix[:, i:i + n, j:j + n]
            submatrix_count += np.sum(submatrix == 60) == m * n * n
    return submatrix_count