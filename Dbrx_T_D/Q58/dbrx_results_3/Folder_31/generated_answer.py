import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    matrix_shape = matrix.shape
    for row in range(matrix_shape[0] - 5):
        for col in range(matrix_shape[1] - 5):
            submatrix = matrix[row:row + 6, col:col + 6]
            if np.isin(45, submatrix).any():
                submatrix_count += 1
    return submatrix_count