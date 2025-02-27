import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 144
    matrix_rows, matrix_cols = matrix.shape
    counter = 0
    for i in range(matrix_rows - n + 1):
        for j in range(matrix_cols - n + 1):
            if np.sum(matrix[i:i + n, j:j + n]) == n * n:
                counter += 1
    return counter