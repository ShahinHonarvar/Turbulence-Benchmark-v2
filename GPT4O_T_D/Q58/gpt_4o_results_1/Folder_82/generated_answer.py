import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    if rows * cols < 99:
        return 0
    count = 0
    for start_row in range(rows):
        for start_col in range(cols):
            for sub_row in range(start_row, rows):
                for sub_col in range(start_col, cols):
                    submatrix_size = (sub_row - start_row + 1) * (sub_col - start_col + 1)
                    if submatrix_size == 99:
                        count += 1
    return count