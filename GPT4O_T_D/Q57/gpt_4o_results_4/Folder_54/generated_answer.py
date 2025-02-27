import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_sum(submatrix):
        return np.sum(submatrix)
    rows, cols = matrix.shape
    submatrices = []
    for top in range(rows):
        for bottom in range(top, rows):
            for left in range(cols):
                for right in range(left, cols):
                    submatrix = matrix[top:bottom + 1, left:right + 1]
                    if get_sum(submatrix) == -59:
                        submatrices.append(submatrix)
    return submatrices