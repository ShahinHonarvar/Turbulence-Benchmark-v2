import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n, m = matrix.shape
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    submatrix_sum = np.sum(matrix[i:k + 1, j:l + 1])
                    if submatrix_sum == -3:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices