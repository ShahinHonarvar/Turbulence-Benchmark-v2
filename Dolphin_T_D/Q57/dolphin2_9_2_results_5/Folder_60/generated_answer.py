import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):
    M, N = matrix.shape
    indices = list(range(1 << M))
    submatrices = []
    for comb in combinations(indices, M - 1):
        submatrix = matrix[comb]
        if np.sum(submatrix) == 94:
            submatrices.append(submatrix)
    return submatrices