import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(matrix, top, left, bottom, right):
        return np.sum(matrix[top:bottom + 1, left:right + 1])
    result = []
    rows, cols = matrix.shape
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    if sum_submatrix(matrix, top, left, bottom, right) == -863:
                        submatrix = matrix[top:bottom + 1, left:right + 1]
                        result.append(submatrix)
    return result