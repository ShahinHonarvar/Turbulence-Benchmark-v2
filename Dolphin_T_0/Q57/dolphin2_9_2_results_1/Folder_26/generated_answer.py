import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    sub = matrix[i:k + 1, j:l + 1]
                    if np.sum(sub) == 997:
                        submatrices.append(sub.tolist())
    return submatrices