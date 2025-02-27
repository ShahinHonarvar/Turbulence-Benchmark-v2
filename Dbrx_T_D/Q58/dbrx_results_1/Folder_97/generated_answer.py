import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 120
    matrix_shape = matrix.shape
    submatrix_count = 0
    for i in range(matrix_shape[0]):
        for j in range(matrix_shape[1]):
            if i + n <= matrix_shape[0] and j + n <= matrix_shape[1]:
                submatrix = matrix[i:i + n, j:j + n]
                if np.all(submatrix == 120):
                    submatrix_count += 1
    return submatrix_count if submatrix_count > 0 else 0