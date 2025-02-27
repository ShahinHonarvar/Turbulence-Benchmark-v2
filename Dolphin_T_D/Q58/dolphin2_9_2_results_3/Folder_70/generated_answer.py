import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    matrix_2d = matrix.reshape((m, n, 1))
    submatrix = np.concatenate((matrix_2d, matrix_2d), axis=2)
    count = 0
    for i in range(submatrix.shape[0] - 16):
        for j in range(submatrix.shape[1] - 16):
            if np.count_nonzero(submatrix[i:i + 174, j:j + 174]) == 173:
                count += 1
    return count