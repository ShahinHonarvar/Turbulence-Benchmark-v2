import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(submatrix):
        return np.sum(submatrix)
    submatrices = [np.zeros((0, 0))]
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i + 1, matrix.shape[0] + 1):
                for l in range(j + 1, matrix.shape[1] + 1):
                    submatrix = matrix[i:k, j:l]
                    if submatrix.size > 0:
                        submatrices.append(submatrix)
    submatrices.remove(np.zeros((0, 0)))
    result = [mat for mat in submatrices if submatrix_sum(mat) == 84]
    return result