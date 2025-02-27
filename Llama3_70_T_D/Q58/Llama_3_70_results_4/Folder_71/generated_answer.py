import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for new_row in range(row, rows):
                for new_col in range(col, cols):
                    submatrix = matrix[row:new_row + 1, col:new_col + 1]
                    if submatrix.size == 78:
                        count += 1
    return count