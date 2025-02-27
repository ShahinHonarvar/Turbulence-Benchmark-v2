import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 54
    matrix_height, matrix_width = matrix.shape
    sub_matrix_counter = 0
    for i in range(matrix_height):
        for j in range(matrix_width):
            if i + n <= matrix_height and j + n <= matrix_width:
                sub_matrix = matrix[i:i + n, j:j + n]
                if np.all(sub_matrix == np.roll(sub_matrix, -1, axis=0)) and np.all(sub_matrix == np.roll(sub_matrix, -1, axis=1)):
                    sub_matrix_counter += 1
    return sub_matrix_counter