import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    matrix_size = matrix.shape
    for i in range(matrix_size[0]):
        for j in range(matrix_size[1]):
            for x in range(i + 1, matrix_size[0]):
                for y in range(j + 1, matrix_size[1]):
                    if np.sum(matrix[i:x + 1, j:y + 1]) == -82:
                        result.append(matrix[i:x + 1, j:y + 1])
    return result