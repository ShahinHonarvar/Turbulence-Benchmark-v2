import numpy as np
import itertools

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for r1, r2 in itertools.product(range(rows), repeat=2):
        for c1, c2 in itertools.product(range(cols), repeat=2):
            if r1 <= r2 and c1 <= c2:
                submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                if np.sum(submatrix) == 66:
                    submatrices.append(submatrix)
    return submatrices