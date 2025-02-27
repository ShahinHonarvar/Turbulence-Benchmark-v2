import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(matrix, top, left, bottom, right):
        return matrix[top:bottom + 1, left:right + 1].sum()
    rows, cols = matrix.shape
    submatrices = []
    target_sum = 8
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    if get_submatrix_sum(matrix, top, left, bottom, right) == target_sum:
                        submatrices.append(matrix[top:bottom + 1, left:right + 1].tolist())
    return submatrices