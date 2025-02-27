import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):
    submatrices = []
    size = len(matrix[0])
    for i in range(size):
        for j in range(size):
            for k in range(i, size):
                for l in range(j, size):
                    if np.sum(matrix[i:k + 1, j:l + 1]) == -87:
                        submatrices.append(matrix[i:k + 1, j:l + 1].tolist())
    return submatrices