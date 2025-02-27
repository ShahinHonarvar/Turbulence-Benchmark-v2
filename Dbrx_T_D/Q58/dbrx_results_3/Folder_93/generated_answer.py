import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    matrix_shape = matrix.shape
    for i in range(matrix_shape[0] - 3):
        for j in range(matrix_shape[1] - 3):
            submatrix = matrix[i:i + 4, j:j + 4]
            if np.isin(submatrix, [53]).sum() == 53:
                submatrix_count += 1
    return submatrix_count