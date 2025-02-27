import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            for z in range(matrix.shape[0] - x):
                for a in range(matrix.shape[1] - y):
                    submatrix = matrix[x:x + z + 1, y:y + a + 1]
                    if np.sum(submatrix) == 862:
                        submatrices.append(submatrix)
    return submatrices