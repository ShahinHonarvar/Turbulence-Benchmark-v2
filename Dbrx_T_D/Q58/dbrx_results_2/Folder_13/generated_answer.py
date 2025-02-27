import numpy as np

def submatrix_with_n_numbers(matrix):
    n, m = matrix.shape
    count = 0
    for i in range(n - 7):
        for j in range(m - 7):
            submatrix = matrix[i:i + 8, j:j + 8]
            if np.isin(submatrix, 175).all():
                count += 1
    return count