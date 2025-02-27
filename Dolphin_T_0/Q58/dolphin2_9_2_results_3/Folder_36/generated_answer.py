import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    matrix_size = matrix.shape
    for i in range(matrix_size[0]):
        for j in range(matrix_size[1]):
            if matrix[i, j] == 131:
                if i + 1 < matrix_size[0]:
                    if matrix[i + 1, j] == 131:
                        count += 1
                if j + 1 < matrix_size[1]:
                    if matrix[i, j + 1] == 131:
                        count += 1
    return count