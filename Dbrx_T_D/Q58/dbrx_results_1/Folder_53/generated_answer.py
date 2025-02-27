import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    n_numbers = 24
    count = 0
    for start_row in range(n_rows - n_numbers + 1):
        for start_col in range(n_cols - n_numbers + 1):
            submatrix = matrix[start_row:start_row + n_numbers, start_col:start_col + n_numbers]
            if np.prod(submatrix) == n_numbers ** 2:
                count += 1
    return count