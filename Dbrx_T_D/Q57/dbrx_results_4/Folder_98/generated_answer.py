import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(submatrix, row, col, submatrices, target_sum):
        if row == submatrix.shape[0] or col == submatrix.shape[1]:
            if submatrix.sum() == target_sum:
                submatrices.append(submatrix.copy())
            return
        submatrix[row, col] = matrix[row, col]
        find_submatrices_with_sum(submatrix, row + 1, col, submatrices, target_sum)
        if col + 1 < submatrix.shape[1]:
            find_submatrices_with_sum(submatrix, row, col + 1, submatrices, target_sum)
        submatrix[row, col] = 0
    submatrices = []
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            find_submatrices_with_sum(np.zeros((matrix.shape[0], matrix.shape[1])), row, col, submatrices, 0)
    return submatrices