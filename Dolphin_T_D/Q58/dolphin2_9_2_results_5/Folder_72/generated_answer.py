import numpy as np

def submatrix_with_n_numbers(matrix):
    n_submatrices = 0
    height, width = matrix.shape
    for i in range(height - 3):
        for j in range(width - 3):
            if np.prod(matrix[i:i + 4, j:j + 4]) == 16:
                n_submatrices += 1
    return n_submatrices