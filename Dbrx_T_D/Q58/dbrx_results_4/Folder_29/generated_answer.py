import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 19
    matrix_shape = matrix.shape
    for i in range(matrix_shape[0] - n + 1):
        for j in range(matrix_shape[1] - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.all(submatrix == 19):
                count += 1
    return count