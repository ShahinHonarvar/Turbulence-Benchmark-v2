import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for r in range(1, m + 1):
        for c in range(1, n + 1):
            if matrix[r - 1:r + 1, c - 1:c + 1].sum() == 66:
                submatrices.append(matrix[r - 1:r + 1, c - 1:c + 1])
    return submatrices