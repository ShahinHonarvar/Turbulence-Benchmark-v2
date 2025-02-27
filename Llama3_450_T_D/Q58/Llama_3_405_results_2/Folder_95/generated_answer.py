import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 87
    for row in range(rows):
        for col in range(cols):
            rows_left = rows - row
            cols_left = cols - col
            for sub_row in range(1, rows_left + 1):
                for sub_col in range(1, cols_left + 1):
                    if sub_row * sub_col == n:
                        sub_matrix = matrix[row:row + sub_row, col:col + sub_col]
                        if np.size(sub_matrix) == n:
                            count += 1
    return count