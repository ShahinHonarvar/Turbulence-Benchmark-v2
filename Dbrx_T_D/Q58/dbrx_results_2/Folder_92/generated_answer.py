import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    count = 0
    for row in range(num_rows - 2):
        for col in range(num_cols - 2):
            submatrix = matrix[row:row + 3, col:col + 3]
            if np.isin(submatrix, 8).sum() == 8:
                count += 1
    return count