import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    matrix_shape = matrix.shape
    for i in range(matrix_shape[0] - 3 + 1):
        for j in range(matrix_shape[1] - 3 + 1):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.isin(submatrix, 74).sum() == 74:
                count += 1
    return count