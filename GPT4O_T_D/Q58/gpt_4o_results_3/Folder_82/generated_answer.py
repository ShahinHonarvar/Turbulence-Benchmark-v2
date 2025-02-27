import numpy as np

def submatrix_with_n_numbers(matrix):
    row_count, col_count = matrix.shape
    submatrix_rows = 99
    submatrix_cols = 1
    total_submatrices = 0
    if row_count * col_count < 99:
        return 0
    for row_start in range(row_count):
        for col_start in range(col_count):
            elements_count = 0
            for r in range(row_start, min(row_count, row_start + submatrix_rows)):
                for c in range(col_start, min(col_count, col_start + submatrix_cols)):
                    elements_count += 1
                    if elements_count > 99:
                        break
            if elements_count == 99:
                total_submatrices += 1
    return total_submatrices