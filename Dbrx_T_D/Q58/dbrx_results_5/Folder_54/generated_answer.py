import numpy as np

def submatrix_with_n_numbers(matrix):
    matrix_shape = matrix.shape
    submatrix_count = 0
    for row in range(matrix_shape[0] - 2):
        for col in range(matrix_shape[1] - 2):
            submatrix = matrix[row:row + 3, col:col + 3]
            if np.isin(27, submatrix).any():
                submatrix_count += 1
    return submatrix_count