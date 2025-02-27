import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for a in range(i + 1, matrix.shape[0] + 1):
                for b in range(j + 1, matrix.shape[1] + 1):
                    if np.sum(matrix[i:a, j:b]) == -61:
                        result.append(matrix[i:a, j:b])
    return result