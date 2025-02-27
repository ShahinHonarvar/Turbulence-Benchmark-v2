import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for top in range(matrix.shape[0]):
        for bottom in range(top, matrix.shape[0]):
            for left in range(matrix.shape[1]):
                for right in range(left, matrix.shape[1]):
                    submatrix = matrix[top:bottom + 1, left:right + 1]
                    if np.sum(submatrix) == -10:
                        submatrices.append(submatrix)
    return submatrices