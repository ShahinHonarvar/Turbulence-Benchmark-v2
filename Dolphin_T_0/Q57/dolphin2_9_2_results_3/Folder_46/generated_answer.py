import numpy as np

def submatrix_with_particular_sum(matrix):
    _, m, n = matrix.shape
    submatrices = []
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    if np.sum(matrix[i:k + 1, j:l + 1]) == 416:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices