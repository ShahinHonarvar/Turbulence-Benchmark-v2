import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.size < 54:
        return 0
    submatrix_count = 0
    matrix_shape = matrix.shape
    submatrix_shape = (6, 9)
    for i in range(matrix_shape[0] - 5):
        for j in range(matrix_shape[1] - 8):
            submatrix = matrix[i:i + 6, j:j + 9]
            if submatrix.size == 54:
                submatrix_count += 1
    return submatrix_count