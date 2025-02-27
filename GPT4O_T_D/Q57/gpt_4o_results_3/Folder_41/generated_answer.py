import numpy as np

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    result = []
    for r1 in range(nrows):
        for r2 in range(r1, nrows):
            for c1 in range(ncols):
                for c2 in range(c1, ncols):
                    submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                    if np.sum(submatrix) == -26:
                        result.append(submatrix.tolist())
    return result