import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    target_size = 60
    for row in range(rows):
        for col in range(cols):
            curr_size = 0
            for sub_row in range(row, rows):
                curr_size += cols - col
                if curr_size >= target_size:
                    count += 1
            curr_size = 0
            for sub_col in range(col, cols):
                curr_size += rows - row
                if curr_size >= target_size:
                    count += 1
    return count