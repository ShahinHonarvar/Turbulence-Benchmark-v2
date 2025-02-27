import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    matrix_shape = matrix.shape
    if matrix_shape[0] < 130 or matrix_shape[1] < 130:
        return submatrix_count
    for row in range(matrix_shape[0] - 130 + 1):
        for col in range(matrix_shape[1] - 130 + 1):
            submatrix = matrix[row:row + 130, col:col + 130]
            if np.isin(submatrix, np.array([130])).all():
                submatrix_count += 1
    return submatrix_count