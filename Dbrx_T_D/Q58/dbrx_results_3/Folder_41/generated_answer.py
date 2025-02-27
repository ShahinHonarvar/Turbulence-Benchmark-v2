import numpy as np

def submatrix_with_n_numbers(matrix):
    n, m = matrix.shape
    count = 0
    for i in range(n - 2):
        for j in range(m - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.isin(submatrix, np.array([73])).all():
                count += 1
    return count