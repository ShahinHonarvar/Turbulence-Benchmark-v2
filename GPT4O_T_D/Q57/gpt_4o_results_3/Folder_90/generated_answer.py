import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_sum_submatrix(matrix, top, left, bottom, right):
        return np.sum(matrix[top:bottom + 1, left:right + 1])
    rows, cols = matrix.shape
    submatrices = []
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    if find_sum_submatrix(matrix, top, left, bottom, right) == -452:
                        submatrices.append(matrix[top:bottom + 1, left:right + 1])
    return submatrices