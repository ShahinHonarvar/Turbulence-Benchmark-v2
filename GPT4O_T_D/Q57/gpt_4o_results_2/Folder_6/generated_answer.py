import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(mat, top, left, bottom, right):
        return np.sum(mat[top:bottom + 1, left:right + 1])
    rows, cols = matrix.shape
    result = []
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    if get_submatrix_sum(matrix, top, left, bottom, right) == 126:
                        submatrix = matrix[top:bottom + 1, left:right + 1]
                        result.append(submatrix.tolist())
    return result