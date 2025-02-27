import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    matrix_shape = matrix.shape
    for row in range(matrix_shape[0] - 1):
        for col in range(matrix_shape[1] - 1):
            submatrix = matrix[row:row + 2, col:col + 2]
            if np.isin(submatrix, 8).sum() == 8:
                submatrix_count += 1
    return submatrix_count