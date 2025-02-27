import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n_rows, n_cols = matrix.shape
    for i in range(n_rows - 7):
        for j in range(n_cols - 6):
            submatrix = matrix[i:i + 8, j:j + 7]
            if np.isin(submatrix, 76).all():
                count += 1
    return count