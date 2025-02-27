import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(mat, top, left, bottom, right):
        submatrix = mat[top:bottom + 1, left:right + 1]
        return np.sum(submatrix)
    result = []
    rows, cols = matrix.shape
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    if get_submatrix_sum(matrix, top, left, bottom, right) == -37:
                        submatrix = matrix[top:bottom + 1, left:right + 1].tolist()
                        result.append(submatrix)
    return result