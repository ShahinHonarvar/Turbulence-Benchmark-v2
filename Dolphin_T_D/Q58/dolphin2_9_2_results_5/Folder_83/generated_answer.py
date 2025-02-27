import numpy as np

def submatrix_with_n_numbers(matrix):
    height, width = matrix.shape
    counter = 0
    for start_row in range(height):
        for start_col in range(width - 46):
            if matrix[start_row:start_row + 5, start_col:start_col + 47].sum() == 47:
                counter += 1
    return counter