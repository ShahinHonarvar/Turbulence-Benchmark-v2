import numpy as np

def submatrix_with_n_numbers(matrix):
    matrix_height, matrix_width = matrix.shape
    count = 0
    for i in range(matrix_height - 1):
        for j in range(matrix_width - 1):
            if np.sum(matrix[i:i + 12, j:j + 8]) == 96:
                count += 1
    return count