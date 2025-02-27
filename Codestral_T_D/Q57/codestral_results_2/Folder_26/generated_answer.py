import numpy as np
import itertools

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for r1, r2 in itertools.product(range(rows), range(rows)):
        for c1, c2 in itertools.product(range(cols), range(cols)):
            if r1 <= r2 and c1 <= c2:
                submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                if submatrix.sum() == 997:
                    submatrices.append(submatrix)
    return submatrices