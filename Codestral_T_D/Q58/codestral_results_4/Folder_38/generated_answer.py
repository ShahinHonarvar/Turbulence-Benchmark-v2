import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for row in range(rows):
        for col in range(cols):
            for sub_rows in range(row, rows):
                for sub_cols in range(col, cols):
                    submatrix = matrix[row:sub_rows + 1, col:sub_cols + 1]
                    if submatrix.size == 34:
                        count += 1
    return count