import numpy as np
import itertools

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for r1, c1 in itertools.product(range(rows), range(cols)):
        for r2, c2 in itertools.product(range(r1, rows), range(c1, cols)):
            submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
            if np.sum(submatrix) == 15:
                submatrices.append(submatrix)
    return submatrices