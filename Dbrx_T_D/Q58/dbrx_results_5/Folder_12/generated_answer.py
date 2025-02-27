import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows - 5):
        for j in range(n_cols - 5):
            submatrix = matrix[i:i + 6, j:j + 6]
            if np.isin(submatrix, 46).all():
                count += 1
    return count