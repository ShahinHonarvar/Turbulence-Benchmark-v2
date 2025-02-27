import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 23
    rows, cols = matrix.shape
    count = 0
    for start_row in range(rows):
        for start_col in range(cols):
            for sub_rows in range(1, rows - start_row + 1):
                for sub_cols in range(1, cols - start_col + 1):
                    if sub_rows * sub_cols == n:
                        submatrix = matrix[start_row:start_row + sub_rows, start_col:start_col + sub_cols]
                        count += 1
    return count