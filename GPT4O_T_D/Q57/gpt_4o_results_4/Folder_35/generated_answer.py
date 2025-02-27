import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(top, left, bottom, right):
        return np.sum(matrix[top:bottom + 1, left:right + 1])
    rows, cols = matrix.shape
    submatrices = []
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    if submatrix_sum(top, left, bottom, right) == 432:
                        submatrices.append(matrix[top:bottom + 1, left:right + 1])
    return submatrices