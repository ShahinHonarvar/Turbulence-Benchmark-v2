import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    shape = matrix.shape
    for i in range(shape[0]):
        for j in range(shape[1]):
            for row in range(i, shape[0]):
                for col in range(j, shape[1]):
                    sub = matrix[i:row + 1, j:col + 1]
                    if np.sum(sub) == -82:
                        submatrices.append(sub)
    return submatrices