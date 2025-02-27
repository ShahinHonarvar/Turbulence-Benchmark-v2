import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    matrix_shape = matrix.shape
    for i in range(matrix_shape[0] - 7):
        for j in range(matrix_shape[1] - 7):
            submatrix = matrix[i:i + 8, j:j + 8]
            if np.isin(submatrix, 49).all():
                count += 1
    return count