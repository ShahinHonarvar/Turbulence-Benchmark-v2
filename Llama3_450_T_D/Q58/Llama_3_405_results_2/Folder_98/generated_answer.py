import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for row in range(rows):
        for col in range(cols):
            for sub_row in range(row + 1, min(row + 4, rows + 1)):
                for sub_col in range(col + 1, min(col + 4, cols + 1)):
                    sub_matrix = matrix[row:sub_row, col:sub_col]
                    if sub_matrix.size == 9:
                        count += 1
    return count