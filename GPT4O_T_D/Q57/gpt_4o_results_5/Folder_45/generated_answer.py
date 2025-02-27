import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(matrix, top, left, bottom, right):
        return matrix[top:bottom, left:right].sum()
    rows, cols = matrix.shape
    result = []
    for top in range(rows):
        for bottom in range(top + 1, rows + 1):
            for left in range(cols):
                for right in range(left + 1, cols + 1):
                    if sum_submatrix(matrix, top, left, bottom, right) == -77:
                        result.append(matrix[top:bottom, left:right].copy())
    return result