import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    for row in range(rows):
        for col in range(cols):
            for submatrix_row in range(row, rows):
                for submatrix_col in range(col, cols):
                    submatrix = matrix[row:submatrix_row + 1, col:submatrix_col + 1]
                    if submatrix.size == 120:
                        count += 1
    return count