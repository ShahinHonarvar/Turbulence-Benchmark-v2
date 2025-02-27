import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            for x in range(i, m):
                for y in range(j, n):
                    sub = matrix[i:x + 1, j:y + 1]
                    if np.sum(sub) == -863:
                        submatrices.append(sub)
    return submatrices