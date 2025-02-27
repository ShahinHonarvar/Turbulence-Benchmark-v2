import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_sum(matrix, top, left, bottom, right):
        total_sum = np.sum(matrix[top:bottom + 1, left:right + 1])
        return total_sum
    rows, cols = matrix.shape
    submatrices = []
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    if get_sum(matrix, top, left, bottom, right) == 64:
                        submatrices.append(matrix[top:bottom + 1, left:right + 1].copy())
    return submatrices