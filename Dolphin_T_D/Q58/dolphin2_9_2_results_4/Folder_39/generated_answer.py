import numpy as np

def submatrix_with_n_numbers(matrix):
    num_to_find = 59
    matrix_counts = 0
    matrix_shape = matrix.shape
    for i in range(matrix_shape[0]):
        for j in range(matrix_shape[1] - num_to_find + 1):
            for k in range(matrix_shape[2] - num_to_find + 1):
                if np.all(matrix[i, j:j + num_to_find, k:k + num_to_find] == num_to_find):
                    matrix_counts += 1
    return matrix_counts