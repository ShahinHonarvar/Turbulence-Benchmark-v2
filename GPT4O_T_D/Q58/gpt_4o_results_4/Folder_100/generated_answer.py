import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    submatrix_count = 0
    for start_row in range(n_rows):
        for start_col in range(n_cols):
            for end_row in range(start_row, n_rows):
                for end_col in range(start_col, n_cols):
                    num_elements = (end_row - start_row + 1) * (end_col - start_col + 1)
                    if num_elements == 10:
                        submatrix_count += 1
    return submatrix_count