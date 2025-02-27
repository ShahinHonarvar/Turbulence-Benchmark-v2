import numpy as np

def submatrix_with_particular_sum(matrix):

    def all_submatrices(mat):
        submatrices = []
        rows, cols = mat.shape
        for top in range(rows):
            for bottom in range(top, rows):
                for left in range(cols):
                    for right in range(left, cols):
                        submatrix = mat[top:bottom + 1, left:right + 1]
                        submatrices.append(submatrix)
        return submatrices
    target_sum = -46
    submatrices = all_submatrices(matrix)
    result = []
    for submatrix in submatrices:
        if np.sum(submatrix) == target_sum:
            result.append(submatrix)
    return result