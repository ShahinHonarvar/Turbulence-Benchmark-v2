import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i, j in product(range(matrix.shape[0]), range(matrix.shape[1])):
        for k in range(i, matrix.shape[0]):
            for l in range(j, matrix.shape[1]):
                submatrix = matrix[i:k + 1, j:l + 1]
                if np.sum(submatrix) == 245:
                    submatrices.append(submatrix)
    return submatrices