import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for r1, r2 in combinations(range(rows + 1), 2):
        for c1, c2 in combinations(range(cols + 1), 2):
            submatrix = matrix[r1:r2, c1:c2]
            if np.sum(submatrix) == -137:
                submatrices.append(submatrix)
    return submatrices