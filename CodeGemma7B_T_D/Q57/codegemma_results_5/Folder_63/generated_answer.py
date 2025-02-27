import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for r1 in range(matrix.shape[0]):
        for r2 in range(r1, matrix.shape[0]):
            for c1 in range(matrix.shape[1]):
                for c2 in range(c1, matrix.shape[1]):
                    submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                    if np.sum(submatrix) == 64:
                        result.append(submatrix)
    return result