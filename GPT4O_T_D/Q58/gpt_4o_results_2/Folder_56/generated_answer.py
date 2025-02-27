import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for start_row in range(rows):
        for end_row in range(start_row, rows):
            for start_col in range(cols):
                for end_col in range(start_col, cols):
                    num_elements = (end_row - start_row + 1) * (end_col - start_col + 1)
                    if num_elements == 68:
                        count += 1
    return count