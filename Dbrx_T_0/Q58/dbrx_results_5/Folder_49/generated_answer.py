import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows - 1):
        for j in range(n_cols - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if np.isin(submatrix, 72).all():
                count += 1
    return count