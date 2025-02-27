import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for sub_rows in range(row + 1, rows + 1):
                for sub_cols in range(col + 1, cols + 1):
                    submatrix = matrix[row:sub_rows, col:sub_cols]
                    if submatrix.size == 57:
                        count += 1
    return count