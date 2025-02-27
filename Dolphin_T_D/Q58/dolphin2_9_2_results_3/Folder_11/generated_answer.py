import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    matrix_size = matrix.shape
    for i in range(matrix_size[0]):
        for j in range(matrix_size[1]):
            for k in range(i, matrix_size[0]):
                for l in range(j, matrix_size[1]):
                    if np.sum(matrix[i:k + 1, j:l + 1]) == 38:
                        count += 1
    return count