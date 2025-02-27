import numpy as np

def submatrix_with_n_numbers(matrix):
    matrix_height = matrix.shape[0]
    matrix_width = matrix.shape[1]
    submatrix_count = 0
    for row_start in range(matrix_height - 2):
        for row_end in range(row_start + 3, matrix_height + 1):
            for col_start in range(matrix_width - 2):
                for col_end in range(col_start + 3, matrix_width + 1):
                    submatrix = matrix[row_start:row_end, col_start:col_end]
                    if np.isin(submatrix, [191]).all():
                        submatrix_count += 1
    return submatrix_count