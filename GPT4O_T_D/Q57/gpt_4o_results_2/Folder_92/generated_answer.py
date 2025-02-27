import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_of_submatrix(mat, top, left, bottom, right):
        return np.sum(mat[top:bottom + 1, left:right + 1])
    rows, cols = matrix.shape
    result = []
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    if sum_of_submatrix(matrix, top, left, bottom, right) == -3:
                        submatrix = matrix[top:bottom + 1, left:right + 1]
                        result.append(submatrix.tolist())
    return result