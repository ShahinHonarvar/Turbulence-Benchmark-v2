import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for r1, r2 in np.ndindex(matrix.shape):
        for c1, c2 in np.ndindex(matrix.shape):
            if c1 <= c2 and r1 <= r2:
                submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                if np.sum(submatrix) == 432:
                    result.append(submatrix)
    return result