import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(top, bottom, left, right):
        return np.sum(matrix[top:bottom + 1, left:right + 1])
    rows, cols = matrix.shape
    target_sum = -137
    submatrices = []
    for top in range(rows):
        for bottom in range(top, rows):
            for left in range(cols):
                for right in range(left, cols):
                    if get_submatrix_sum(top, bottom, left, right) == target_sum:
                        submatrices.append(matrix[top:bottom + 1, left:right + 1].copy())
    return submatrices