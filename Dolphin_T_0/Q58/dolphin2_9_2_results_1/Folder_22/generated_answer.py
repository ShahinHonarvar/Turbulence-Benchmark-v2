import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.size < 21:
        return 0
    result = 0
    matrix_shape = matrix.shape
    matrix_size = matrix_shape[0] * matrix_shape[1]
    for i in range(matrix_shape[0]):
        for j in range(matrix_shape[1]):
            for x in range(i + 2, matrix_shape[0] + 1):
                for y in range(j + 2, matrix_shape[1] + 1):
                    submatrix = matrix[i:x, j:y]
                    if submatrix.size == 21:
                        result += 1
    return result