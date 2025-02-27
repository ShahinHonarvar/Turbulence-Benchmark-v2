import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(submatrix):
        return np.sum(submatrix)

    def find_submatrices_with_sum(matrix, target_sum):
        rows, cols = matrix.shape
        submatrices = []
        for r1 in range(rows):
            for r2 in range(r1, rows):
                for c1 in range(cols):
                    for c2 in range(c1, cols):
                        submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                        if get_submatrix_sum(submatrix) == target_sum:
                            submatrices.append(submatrix)
        return submatrices
    return find_submatrices_with_sum(matrix, -42)