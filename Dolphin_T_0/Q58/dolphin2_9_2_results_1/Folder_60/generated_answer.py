import numpy as np

def submatrix_with_n_numbers(matrix):
    num_of_submatrices = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i, j] == 88:
                num_of_submatrices += 1
    return num_of_submatrices if num_of_submatrices != 0 else 0