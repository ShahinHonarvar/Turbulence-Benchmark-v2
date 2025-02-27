import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    matrix = np.asarray(matrix)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for x in range(i + 1, matrix.shape[0]):
                for y in range(j + 1, matrix.shape[1]):
                    if np.sum(matrix[i:x, j:y]) == -77:
                        submatrices.append(matrix[i:x, j:y])
    return submatrices