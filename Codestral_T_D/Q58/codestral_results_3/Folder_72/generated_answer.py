import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for row_start in range(rows - 3):
        for col_start in range(cols - 3):
            if np.sum(matrix[row_start:row_start + 4, col_start:col_start + 4]) == 16 * 4:
                count += 1
    return count