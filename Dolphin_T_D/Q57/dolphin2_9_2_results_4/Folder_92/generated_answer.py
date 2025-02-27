import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    x = 0
    while x < m:
        for y in range(x, n):
            if np.sum(matrix[x:y + 1, x:y + 1]) == -3:
                return matrix[x:y + 1, x:y + 1].tolist()
            elif y == n:
                x = x + 1
    return []