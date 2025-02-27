import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray):
        matrix = np.array(matrix)
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    sub = np.sum(matrix[i:k + 1, j:l + 1])
                    if sub == -93:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices