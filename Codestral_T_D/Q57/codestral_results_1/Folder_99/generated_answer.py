import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for i, j, x, y in product(range(rows), repeat=4):
        if i <= x and j <= y:
            submatrix = matrix[i:x + 1, j:y + 1]
            if np.sum(submatrix) == -185:
                submatrices.append(submatrix)
    return submatrices