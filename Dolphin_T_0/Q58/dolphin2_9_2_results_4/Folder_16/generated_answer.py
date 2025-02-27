import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrices_count = 0
    matrix_shape = matrix.shape
    for i in range(matrix_shape[0]):
        for j in range(matrix_shape[1]):
            if i + 13 < matrix_shape[0] and j + 13 < matrix_shape[1]:
                if np.count_nonzero(matrix[i:i + 14, j:j + 14]) == 154:
                    submatrices_count += 1
    return submatrices_count