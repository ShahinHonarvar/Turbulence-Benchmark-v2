import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for row in range(n_rows):
        for col in range(n_cols):
            if row + 8 < n_rows and col + 8 < n_cols:
                submatrix = matrix[row:row + 9, col:col + 9]
                if np.sum(submatrix) == 63:
                    count += 1
    return count