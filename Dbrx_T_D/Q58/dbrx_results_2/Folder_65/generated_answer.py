import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    matrix_shape = matrix.shape
    for row in range(matrix_shape[0] - 4):
        for col in range(matrix_shape[1] - 4):
            submatrix = matrix[row:row + 5, col:col + 5]
            if np.all(submatrix == 35):
                submatrix_count += 1
    return submatrix_count