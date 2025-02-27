import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    if rows * cols < 24:
        return 0
    submatrix_count = 0
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row, rows):
                for end_col in range(start_col, cols):
                    submatrix_elements = (end_row - start_row + 1) * (end_col - start_col + 1)
                    if submatrix_elements == 24:
                        submatrix_count += 1
    return submatrix_count