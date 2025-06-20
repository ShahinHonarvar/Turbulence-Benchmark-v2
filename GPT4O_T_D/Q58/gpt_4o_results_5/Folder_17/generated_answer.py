import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 166
    rows, cols = matrix.shape
    count = 0
    for row_start in range(rows):
        for col_start in range(cols):
            for row_end in range(row_start, rows):
                for col_end in range(col_start, cols):
                    num_elements = (row_end - row_start + 1) * (col_end - col_start + 1)
                    if num_elements == n:
                        count += 1
    return count