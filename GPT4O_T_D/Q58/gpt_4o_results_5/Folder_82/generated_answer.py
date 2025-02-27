import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_size = 99
    total_count = 0
    if rows * cols < submatrix_size:
        return 0
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row, rows):
                for end_col in range(start_col, cols):
                    if (end_row - start_row + 1) * (end_col - start_col + 1) == submatrix_size:
                        total_count += 1
    return total_count