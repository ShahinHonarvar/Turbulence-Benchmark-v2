import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    if np.sum(matrix[i:k + 1, j:l + 1]) == -65:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices if submatrices else []