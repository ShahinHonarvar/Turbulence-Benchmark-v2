import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices_sum(matrix, target_sum):
        rows, cols = matrix.shape
        submatrices = []
        for i in range(rows):
            for j in range(cols):
                for k in range(i, rows):
                    for l in range(j, cols):
                        submatrix = matrix[i:k + 1, j:l + 1]
                        if np.sum(submatrix) == target_sum:
                            submatrices.append(submatrix)
        return submatrices
    return get_submatrices_sum(matrix, 830)