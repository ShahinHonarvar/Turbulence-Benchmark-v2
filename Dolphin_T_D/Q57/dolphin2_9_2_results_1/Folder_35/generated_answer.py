import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):
    submatrices = []
    matrix_sum = matrix.sum()
    if matrix_sum == 432:
        return [matrix]
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in combinations(range(matrix.shape[0]), 2):
                for l in combinations(range(matrix.shape[1]), 2):
                    submatrix = np.array(matrix[k[0]:k[1] + 1, l[0]:l[1] + 1])
                    sum = submatrix.sum()
                    if sum == 432:
                        submatrices.append(submatrix)
    return submatrices