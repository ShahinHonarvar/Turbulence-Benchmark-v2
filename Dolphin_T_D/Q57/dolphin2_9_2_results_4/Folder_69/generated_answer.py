import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):
    n = len(matrix)
    m = len(matrix[0])
    submatrices = []
    for r1 in range(n):
        for r2 in range(r1 + 1, n):
            for c1 in range(m):
                for c2 in range(c1 + 1, m):
                    submatrix = matrix[r1:r2, c1:c2]
                    if np.sum(submatrix) == 752:
                        submatrices.append(submatrix.tolist())
    return submatrices