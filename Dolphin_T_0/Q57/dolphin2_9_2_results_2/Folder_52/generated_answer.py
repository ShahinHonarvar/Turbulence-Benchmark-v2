import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):
    submatrices = []
    indices = list(combinations(range(matrix.shape[0]), 2))
    for i, j in indices:
        for k, l in indices:
            submatrix = matrix[i:j + 1, k:l + 1]
            if np.sum(submatrix) == 100:
                submatrices.append(submatrix)
    return submatrices