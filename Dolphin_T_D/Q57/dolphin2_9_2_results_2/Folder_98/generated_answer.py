import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    matrix = np.array(matrix)
    for r1 in range(matrix.shape[0]):
        for c1 in range(matrix.shape[1]):
            for r2 in range(r1, matrix.shape[0]):
                for c2 in range(c1, matrix.shape[1]):
                    submatrix_sum = np.sum(matrix[r1:r2 + 1, c1:c2 + 1])
                    if submatrix_sum == 0:
                        result.append(matrix[r1:r2 + 1, c1:c2 + 1])
    return result