import numpy as np

def submatrix_with_n_numbers(matrix):
    row_count, col_count = matrix.shape
    count = 0
    for row_start in range(row_count):
        for row_end in range(row_start, row_count):
            for col_start in range(col_count):
                for col_end in range(col_start, col_count):
                    if (row_end - row_start + 1) * (col_end - col_start + 1) == 104:
                        count += 1
    return count