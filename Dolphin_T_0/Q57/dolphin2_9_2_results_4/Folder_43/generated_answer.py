import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):
    size = len(matrix)
    submatrices = []
    for r1 in range(size):
        for r2 in range(r1, size):
            for c1 in range(size):
                for c2 in range(c1, size):
                    submatrix_sum = np.sum(matrix[r1:r2 + 1, c1:c2 + 1])
                    if submatrix_sum == -81:
                        submatrices.append(matrix[r1:r2 + 1, c1:c2 + 1])
    return submatrices