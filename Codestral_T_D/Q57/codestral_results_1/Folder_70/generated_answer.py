import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for i in range(rows + 1):
        for j in range(cols + 1):
            for r in range(i + 1, rows + 1):
                for c in range(j + 1, cols + 1):
                    submatrix = matrix[i:r, j:c]
                    if np.sum(submatrix) == 411:
                        submatrices.append(submatrix)
    return submatrices