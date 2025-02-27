import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    submatrix = np.array(matrix[i:k + 1, j:l + 1])
                    if np.sum(submatrix) == 432:
                        submatrices.append(submatrix)
    if not submatrices:
        return []
    else:
        return submatrices