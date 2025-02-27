import numpy as np

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    result = []
    for top in range(nrows):
        for left in range(ncols):
            for bottom in range(top, nrows):
                for right in range(left, ncols):
                    submatrix = matrix[top:bottom + 1, left:right + 1]
                    if np.sum(submatrix) == 56:
                        result.append(submatrix.tolist())
    return result