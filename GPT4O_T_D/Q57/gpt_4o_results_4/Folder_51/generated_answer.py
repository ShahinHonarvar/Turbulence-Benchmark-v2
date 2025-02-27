import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(matrix, top, left, bottom, right):
        return np.sum(matrix[top:bottom + 1, left:right + 1])

    def find_submatrices_with_sum(matrix, target_sum):
        rows, cols = matrix.shape
        submatrices = []
        for top in range(rows):
            for left in range(cols):
                for bottom in range(top, rows):
                    for right in range(left, cols):
                        if sum_submatrix(matrix, top, left, bottom, right) == target_sum:
                            submatrices.append(matrix[top:bottom + 1, left:right + 1].tolist())
        return submatrices
    return find_submatrices_with_sum(matrix, -46)