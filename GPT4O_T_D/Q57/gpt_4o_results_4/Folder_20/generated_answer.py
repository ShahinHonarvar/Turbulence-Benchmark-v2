import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(top, left, bottom, right):
        submat = matrix[top:bottom + 1, left:right + 1]
        return np.sum(submat)
    rows, cols = matrix.shape
    result = []
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    if get_submatrix_sum(top, left, bottom, right) == -57:
                        submatrix = matrix[top:bottom + 1, left:right + 1].tolist()
                        result.append(submatrix)
    return result