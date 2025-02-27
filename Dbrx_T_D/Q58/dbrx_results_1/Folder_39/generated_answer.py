import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    for row_start in range(matrix.shape[0] - 2):
        for row_end in range(row_start + 3, matrix.shape[0] + 1):
            for col_start in range(matrix.shape[1] - 2):
                for col_end in range(col_start + 3, matrix.shape[1] + 1):
                    submatrix = matrix[row_start:row_end, col_start:col_end]
                    if np.count_nonzero(submatrix == 59) == 59:
                        submatrix_count += 1
    return submatrix_count