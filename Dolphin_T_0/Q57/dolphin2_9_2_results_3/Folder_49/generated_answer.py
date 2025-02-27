import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for r in range(1, matrix.shape[0] + 1):
        for c in range(1, matrix.shape[1] + 1):
            for i, j in combinations(range(matrix.shape[0]), r):
                for k, l in combinations(range(matrix.shape[1]), c):
                    if np.sum(matrix[i:i + r, j:j + c]) == -42:
                        submatrices.append(matrix[i:i + r, j:j + c])
    return submatrices