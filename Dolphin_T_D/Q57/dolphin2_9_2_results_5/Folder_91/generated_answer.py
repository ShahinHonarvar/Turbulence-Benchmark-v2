import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.dtype.kind != 'i':
        raise TypeError('Input must be a numpy matrix of integers')
    submatrices = []
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            for x in range(i + 1, matrix.shape[0] + 1):
                for y in range(j + 1, matrix.shape[1] + 1):
                    if np.sum(matrix[i:x, j:y]) == -6:
                        submatrices.append(matrix[i:x, j:y])
    return submatrices