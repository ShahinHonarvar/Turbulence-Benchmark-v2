import numpy as np

def submatrix_with_n_numbers(matrix):
    row_count, col_count = matrix.shape
    total_elements = row_count * col_count
    if total_elements < 179:
        return 0
    submatrices_count = 0
    for start_row in range(row_count):
        for end_row in range(start_row, row_count):
            for start_col in range(col_count):
                for end_col in range(start_col, col_count):
                    submatrix_size = (end_row - start_row + 1) * (end_col - start_col + 1)
                    if submatrix_size == 179:
                        submatrices_count += 1
    return submatrices_count