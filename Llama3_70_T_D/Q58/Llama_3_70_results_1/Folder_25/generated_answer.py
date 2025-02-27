import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 66
    for row in range(rows):
        for col in range(cols):
            for offset_row in range(rows - row):
                for offset_col in range(cols - col):
                    submatrix = matrix[row:row + offset_row + 1, col:col + offset_col + 1]
                    if submatrix.size == n:
                        count += 1
    return count