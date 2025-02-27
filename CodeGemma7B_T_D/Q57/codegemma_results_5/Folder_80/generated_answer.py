import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    target_sum = 245
    rows, cols = matrix.shape
    submatrices = []
    for i1, i2 in product(range(rows), repeat=2):
        for j1, j2 in product(range(cols), repeat=2):
            submatrix = matrix[i1:i2 + 1, j1:j2 + 1]
            if np.sum(submatrix) == target_sum:
                submatrices.append(submatrix)
    if not submatrices:
        empty_list = []
        return empty_list
    else:
        return submatrices