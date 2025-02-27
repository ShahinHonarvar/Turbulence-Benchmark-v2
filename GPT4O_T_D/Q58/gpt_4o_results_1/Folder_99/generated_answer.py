import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_size = 146
    count = 0
    for start_row in range(rows):
        for start_col in range(cols):
            row_limit = min(rows, start_row + submatrix_size)
            col_limit = min(cols, start_col + submatrix_size)
            submatrix_elements = (row_limit - start_row) * (col_limit - start_col)
            if submatrix_elements == submatrix_size:
                count += 1
    return count