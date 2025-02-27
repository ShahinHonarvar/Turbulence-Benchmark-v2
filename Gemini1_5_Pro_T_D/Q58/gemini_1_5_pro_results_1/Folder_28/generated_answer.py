import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for row_start in range(rows - 36):
        for col_start in range(cols - 36):
            for row_end in range(row_start + 37, rows + 1):
                for col_end in range(col_start + 37, cols + 1):
                    if (row_end - row_start) * (col_end - col_start) == 37:
                        count += 1
    return count