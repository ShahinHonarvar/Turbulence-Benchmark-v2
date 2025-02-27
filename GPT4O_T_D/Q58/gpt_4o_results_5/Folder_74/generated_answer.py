import numpy as np

def submatrix_with_n_numbers(matrix):
    row_count, col_count = matrix.shape
    matrices_count = 0
    for i in range(row_count):
        for j in range(col_count):
            for sub_rows in range(1, row_count - i + 1):
                for sub_cols in range(1, col_count - j + 1):
                    if sub_rows * sub_cols == 48:
                        matrices_count += 1
    return matrices_count