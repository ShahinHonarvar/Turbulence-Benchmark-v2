import numpy as np

def submatrix_with_n_numbers(matrix, n=57):
    row_len, col_len = matrix.shape
    count = 0
    for row_start in range(row_len):
        for col_start in range(col_len):
            for row_end in range(row_start + 1, row_len + 1):
                for col_end in range(col_start + 1, col_len + 1):
                    submatrix = matrix[row_start:row_end, col_start:col_end]
                    if submatrix.size == n:
                        count += (submatrix == 57).all()
    return count