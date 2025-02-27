import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    matrix_shape = matrix.shape
    for i in range(matrix_shape[0] - 1):
        for j in range(matrix_shape[1] - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if np.count_nonzero(submatrix) == 8:
                count += 1
    return count