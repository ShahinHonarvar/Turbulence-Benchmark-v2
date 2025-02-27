import numpy as np

def submatrix_with_n_numbers(matrix):
    row_len, col_len = matrix.shape
    count = 0
    for row_start in range(row_len):
        for col_start in range(col_len):
            for row_size in range(1, row_len + 1 - row_start):
                for col_size in range(1, col_len + 1 - col_start):
                    submatrix = matrix[row_start:row_start + row_size, col_start:col_start + col_size]
                    if submatrix.size == 121 and (submatrix == 121).all():
                        count += 1
    return count