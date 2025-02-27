import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 85
    for row_start in range(rows):
        for row_end in range(row_start + 1, rows + 1):
            if (row_end - row_start) * cols < n:
                continue
            for col_start in range(cols):
                for col_end in range(col_start + 1, cols + 1):
                    if (row_end - row_start) * (col_end - col_start) == n:
                        count += 1
    return count