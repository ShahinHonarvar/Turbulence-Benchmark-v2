import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    total_count = 0
    for start_row in range(rows):
        for end_row in range(start_row, rows):
            for start_col in range(cols):
                for end_col in range(start_col, cols):
                    submatrix_size = (end_row - start_row + 1) * (end_col - start_col + 1)
                    if submatrix_size == 94:
                        total_count += 1
    return total_count