import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 43
    matrix_height, matrix_width = matrix.shape
    if matrix_height < n or matrix_width < n:
        return 0
    submatrix_count = 0
    for i in range(matrix_height - n + 1):
        for j in range(matrix_width - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.isnan(submatrix).any():
                continue
            if np.all(submatrix == 43):
                submatrix_count += 1
    return submatrix_count