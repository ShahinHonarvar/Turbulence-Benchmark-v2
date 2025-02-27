import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(matrix, top, left, bottom, right):
        return np.sum(matrix[top:bottom + 1, left:right + 1])
    rows, cols = matrix.shape
    target_sum = 394
    result = []
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    if get_submatrix_sum(matrix, top, left, bottom, right) == target_sum:
                        result.append(matrix[top:bottom + 1, left:right + 1].tolist())
    return result