import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n, m = matrix.shape
    for i in range(n - 9):
        for j in range(m - 9):
            submatrix = matrix[i:i + 10, j:j + 10]
            if np.isin(submatrix, [90]).all():
                count += 1
    return count