import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    matrix_size = matrix.shape
    for i in range(matrix_size[0] - 1):
        for j in range(matrix_size[1] - 1):
            if np.sum(matrix[i:i + 2, j:j + 2]) == 176:
                count += 1
    return count