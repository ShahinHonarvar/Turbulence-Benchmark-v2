import numpy as np
import itertools

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for shape in itertools.product(range(matrix.shape[0]), range(matrix.shape[1])):
        for start in itertools.product(range(matrix.shape[0] - shape[0] + 1), range(matrix.shape[1] - shape[1] + 1)):
            submatrix = matrix[start[0]:start[0] + shape[0], start[1]:start[1] + shape[1]]
            if np.sum(submatrix) == -77:
                submatrices.append(submatrix)
    return submatrices