import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 39
    matrix_height, matrix_width = matrix.shape
    count = 0
    for row_start in range(matrix_height - n + 1):
        for col_start in range(matrix_width - n + 1):
            submatrix = matrix[row_start:row_start + n, col_start:col_start + n]
            if np.isin(submatrix, 39).all():
                count += 1
    return count