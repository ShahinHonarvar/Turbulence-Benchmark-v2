import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 139
    rows, cols = matrix.shape
    count = 0
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row, rows):
                for end_col in range(start_col, cols):
                    if (end_row - start_row + 1) * (end_col - start_col + 1) == n:
                        count += 1
    return count