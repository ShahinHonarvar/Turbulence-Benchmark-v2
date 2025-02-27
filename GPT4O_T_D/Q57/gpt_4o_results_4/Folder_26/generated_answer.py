import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix(matrix, top, left, bottom, right):
        return matrix[top:bottom + 1, left:right + 1]
    rows, cols = matrix.shape
    result = []
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    submatrix = get_submatrix(matrix, top, left, bottom, right)
                    if np.sum(submatrix) == 997:
                        result.append(submatrix.tolist())
    return result