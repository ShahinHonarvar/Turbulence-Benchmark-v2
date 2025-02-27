import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            if i + 2 < m and j + 2 < n and (np.sum(matrix[i:i + 3, j:j + 3]) == -46):
                submatrices.append(matrix[i:i + 3, j:j + 3])
    return submatrices