import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for start_row in range(rows - 3):
        for start_col in range(cols - 3):
            submatrix = matrix[start_row:start_row + 4, start_col:start_col + 4]
            if submatrix.size == 16:
                count += 1
    return count