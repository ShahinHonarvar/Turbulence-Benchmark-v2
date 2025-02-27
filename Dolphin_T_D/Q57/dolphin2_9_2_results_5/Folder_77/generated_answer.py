import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for i in range(m):
        for j in range(n):
            for a in range(i, m):
                for b in range(j, n):
                    submatrix = matrix[i:a + 1, j:b + 1]
                    if np.sum(submatrix) == -336:
                        submatrices.append(submatrix)
    return submatrices