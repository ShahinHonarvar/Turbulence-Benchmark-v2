import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(1, matrix.shape[0] + 1):
        for j in range(1, matrix.shape[1] + 1):
            for roi in combinations(range(matrix.shape[0]), i):
                for coi in combinations(range(matrix.shape[1]), j):
                    subrectangle = matrix[np.ix_(roi, coi)]
                    if np.sum(subrectangle) == -336:
                        submatrices.append(subrectangle)
    return submatrices