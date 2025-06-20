import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(matrix, top, left, bottom, right):
        return matrix[top:bottom + 1, left:right + 1].sum()
    rows, cols = matrix.shape
    result = []
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    if submatrix_sum(matrix, top, left, bottom, right) == 15:
                        result.append(matrix[top:bottom + 1, left:right + 1].tolist())
    return result