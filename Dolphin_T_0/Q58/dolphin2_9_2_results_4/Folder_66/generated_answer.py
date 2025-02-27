import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 42
    matrix_shape = matrix.shape
    row_count = matrix_shape[0]
    col_count = matrix_shape[1]
    count = 0
    for i in range(row_count - n + 1):
        for j in range(col_count - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.count_nonzero(submatrix == n) == n * n:
                count += 1
    return count