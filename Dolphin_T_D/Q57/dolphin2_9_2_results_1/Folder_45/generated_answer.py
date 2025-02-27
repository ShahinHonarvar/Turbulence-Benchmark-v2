import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(mat):
    submatrices = []
    for r in range(1, mat.shape[0] + 1):
        for c in range(1, mat.shape[1] + 1):
            for combination in combinations(range(mat.shape[0]), r):
                for combination in combinations(range(mat.shape[1]), c):
                    submatrix_sum = np.sum(mat[np.ix_(combination, combination)])
                    if submatrix_sum == -77:
                        submatrices.append(mat[np.ix_(combination, combination)])
    return submatrices if submatrices else []