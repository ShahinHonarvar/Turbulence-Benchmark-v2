import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    matrix_shape = matrix.shape
    for i in range(matrix_shape[0]):
        for j in range(matrix_shape[1]):
            if matrix_shape[0] - i >= 7 and matrix_shape[1] - j >= 7:
                submatrix = matrix[i:i + 7, j:j + 7]
                if len(submatrix) == 49:
                    count += 1
    return count