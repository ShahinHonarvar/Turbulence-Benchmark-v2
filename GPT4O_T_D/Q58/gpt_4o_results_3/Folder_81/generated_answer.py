import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    target_count = 97
    total_count = 0
    for row_start in range(rows):
        for col_start in range(cols):
            for row_end in range(row_start + 1, rows + 1):
                for col_end in range(col_start + 1, cols + 1):
                    if (row_end - row_start) * (col_end - col_start) == target_count:
                        total_count += 1
    return total_count