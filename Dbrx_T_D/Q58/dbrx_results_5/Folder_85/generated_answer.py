import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    matrix_shape = matrix.shape
    for i in range(matrix_shape[0] - 2):
        for j in range(matrix_shape[1] - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.all(submatrix == 13):
                submatrix_count += 1
    return submatrix_count