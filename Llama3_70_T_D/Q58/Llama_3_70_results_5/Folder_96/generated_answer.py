import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    n = 20
    for row in range(rows):
        for col in range(cols):
            for s_row in range(row, rows):
                for s_col in range(col, cols):
                    submatrix = matrix[row:s_row + 1, col:s_col + 1]
                    if submatrix.size == n:
                        count += 1
    return count