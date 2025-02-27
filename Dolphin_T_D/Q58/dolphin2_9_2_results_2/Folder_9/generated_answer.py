import numpy as np

def submatrix_with_n_numbers(matrix):
    counter = 0
    num = 33
    matrix_h = matrix.shape[0]
    matrix_v = matrix.shape[1]
    for i in range(matrix_h - num + 1):
        for j in range(matrix_v - num + 1):
            if np.count_nonzero(matrix[i:i + num, j:j + num]) == num:
                counter += 1
    return counter