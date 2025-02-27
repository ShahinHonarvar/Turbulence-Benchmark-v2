import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(top, left, bottom, right):
        return np.sum(matrix[top:bottom + 1, left:right + 1])
    nrows, ncols = matrix.shape
    submatrices = []
    for top in range(nrows):
        for left in range(ncols):
            for bottom in range(top, nrows):
                for right in range(left, ncols):
                    if get_submatrix_sum(top, left, bottom, right) == -308:
                        submatrices.append(matrix[top:bottom + 1, left:right + 1].tolist())
    return submatrices