import numpy as np

def submatrix_with_particular_sum(matrix):
    if matrix.min() > -36:
        return []
    submatrices = []
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    if np.sum(matrix[i:k + 1, j:l + 1]) == -36:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices