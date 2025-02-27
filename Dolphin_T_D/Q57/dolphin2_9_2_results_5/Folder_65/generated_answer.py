import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for r in range(1, min(rows, cols) + 1):
        for c in combinations(range(cols), r):
            for l in combinations(range(rows), r):
                sub_matrix = matrix[np.ix_(l, c)]
                if np.sum(sub_matrix) == 78:
                    submatrices.append(sub_matrix)
    return submatrices