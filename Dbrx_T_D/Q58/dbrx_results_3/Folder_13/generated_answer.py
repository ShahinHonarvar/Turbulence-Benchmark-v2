import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n_rows, n_cols = matrix.shape
    for i in range(n_rows - 174):
        for j in range(n_cols - 174):
            submatrix = matrix[i:i + 175, j:j + 175]
            if np.isin(submatrix, 175).all():
                count += 1
    return count