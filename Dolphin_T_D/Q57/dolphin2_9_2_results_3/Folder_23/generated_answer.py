import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            for k in range(i + 1, n):
                for l in range(j + 1, m):
                    submatrix = np.array([[matrix[p][q] for q in range(j, l + 1)] for p in range(i, k + 1)])
                    if np.sum(submatrix) == 59:
                        submatrices.append(submatrix.tolist())
    return submatrices