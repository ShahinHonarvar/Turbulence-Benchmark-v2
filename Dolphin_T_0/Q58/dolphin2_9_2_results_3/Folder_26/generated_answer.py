import numpy as np

def submatrix_with_n_numbers(matrix):
    matrix_size = matrix.shape
    counter = 0
    for i in range(matrix_size[0] - 1):
        for j in range(matrix_size[1] - 1):
            if np.sum(matrix[i:i + 2, j:j + 2]) == 115:
                counter += 1
    return counter