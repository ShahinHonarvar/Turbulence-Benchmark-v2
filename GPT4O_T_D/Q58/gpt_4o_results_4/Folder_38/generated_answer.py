import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    count = 0
    target = 34
    for row_start in range(num_rows):
        for col_start in range(num_cols):
            for row_end in range(row_start, num_rows):
                for col_end in range(col_start, num_cols):
                    if (row_end - row_start + 1) * (col_end - col_start + 1) == target:
                        count += 1
    return count