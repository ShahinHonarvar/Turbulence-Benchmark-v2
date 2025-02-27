import numpy as np

def submatrix_with_n_numbers(matrix):
    matrix_shape = matrix.shape
    if matrix_shape[0] < 3 or matrix_shape[1] < 3:
        return 0
    count = 0
    for i in range(matrix_shape[0] - 2):
        for j in range(matrix_shape[1] - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.isin(submatrix, 27).all():
                count += 1
    return count