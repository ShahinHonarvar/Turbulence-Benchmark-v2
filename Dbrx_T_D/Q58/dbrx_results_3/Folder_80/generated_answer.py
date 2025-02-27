import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    matrix_shape = matrix.shape
    for i in range(matrix_shape[0] - 179):
        for j in range(matrix_shape[1] - 179):
            submatrix = matrix[i:i + 180, j:j + 180]
            if np.isin(submatrix, [180]).any():
                submatrix_count += 1
    return submatrix_count