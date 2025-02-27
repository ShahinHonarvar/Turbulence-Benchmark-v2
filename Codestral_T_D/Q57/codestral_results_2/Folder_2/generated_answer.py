import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for lr, lc, hr, hc in product(range(rows), repeat=4):
        if lr <= hr and lc <= hc:
            submatrix = matrix[lr:hr + 1, lc:hc + 1]
            if submatrix.sum() == -863:
                submatrices.append(submatrix)
    return submatrices