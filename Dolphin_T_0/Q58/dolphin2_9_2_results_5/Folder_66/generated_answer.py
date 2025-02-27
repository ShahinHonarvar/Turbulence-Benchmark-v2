import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    matrix_shape = matrix.shape
    for i in range(matrix_shape[0]):
        for j in range(matrix_shape[1]):
            if matrix[i, j] == 42:
                if i + 2 < matrix_shape[0]:
                    for m in range(i, i + 3):
                        if j + 3 < matrix_shape[1]:
                            for n in range(j, j + 4):
                                if matrix[m, n] == 42:
                                    count += 1
    return count