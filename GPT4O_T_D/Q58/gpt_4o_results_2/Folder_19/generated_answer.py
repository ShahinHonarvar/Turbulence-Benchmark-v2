import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    target_size = 17
    for row_start in range(rows):
        for row_end in range(row_start, rows):
            for col_start in range(cols):
                for col_end in range(col_start, cols):
                    if (row_end - row_start + 1) * (col_end - col_start + 1) == target_size:
                        count += 1
    return count