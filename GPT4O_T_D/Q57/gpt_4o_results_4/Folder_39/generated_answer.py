import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices_with_sum(matrix, target):
        R, C = matrix.shape
        submatrices = []
        for i in range(R):
            for j in range(C):
                for r in range(i, R):
                    for c in range(j, C):
                        submatrix = matrix[i:r + 1, j:c + 1]
                        if np.sum(submatrix) == target:
                            submatrices.append(submatrix.tolist())
        return submatrices
    return get_submatrices_with_sum(matrix, 66)