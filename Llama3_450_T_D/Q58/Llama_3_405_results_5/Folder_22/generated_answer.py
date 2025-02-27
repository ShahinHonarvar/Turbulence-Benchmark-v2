import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    for row in range(rows):
        for col in range(cols):
            for sub_rows in range(1, rows - row + 1):
                for sub_cols in range(1, cols - col + 1):
                    if sub_rows * sub_cols == 21:
                        submatrix = matrix[row:row + sub_rows, col:col + sub_cols]
                        count += 1
    return count