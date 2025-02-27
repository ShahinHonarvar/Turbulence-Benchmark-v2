import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for row in range(rows):
        for col in range(cols):
            for sub_rows in range(row + 1, rows + 1):
                for sub_cols in range(col + 1, cols + 1):
                    sub_matrix = matrix[row:sub_rows, col:sub_cols]
                    if sub_matrix.size == 146:
                        count += 1
    return count