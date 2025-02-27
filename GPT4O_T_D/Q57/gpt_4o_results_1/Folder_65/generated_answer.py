import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(matrix, top, bottom, left, right):
        return np.sum(matrix[top:bottom + 1, left:right + 1])
    rows, cols = matrix.shape
    result = []
    for top in range(rows):
        for bottom in range(top, rows):
            for left in range(cols):
                for right in range(left, cols):
                    if submatrix_sum(matrix, top, bottom, left, right) == 78:
                        submatrix = matrix[top:bottom + 1, left:right + 1]
                        result.append(submatrix.tolist())
    return result