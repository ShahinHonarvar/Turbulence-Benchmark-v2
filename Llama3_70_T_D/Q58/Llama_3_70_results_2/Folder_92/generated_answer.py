import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows - 1):
        for col in range(cols - 1):
            for sub_row in range(row + 1, rows):
                for sub_col in range(col + 1, cols):
                    sub_matrix = matrix[row:sub_row + 1, col:sub_col + 1]
                    if sub_matrix.size == 8:
                        count += 1
    return count