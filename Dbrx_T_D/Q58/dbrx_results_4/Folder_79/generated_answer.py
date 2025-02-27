import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    matrix_shape = matrix.shape
    for i in range(matrix_shape[0] - 9):
        for j in range(matrix_shape[1] - 9):
            submatrix = matrix[i:i + 10, j:j + 10]
            if np.count_nonzero(submatrix == 6) == 60:
                submatrix_count += 1
    return submatrix_count