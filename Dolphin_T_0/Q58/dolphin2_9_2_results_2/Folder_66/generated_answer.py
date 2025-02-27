import numpy as np

def submatrix_with_n_numbers(matrix):
    num_of_submatrices = 0
    row, col = matrix.shape
    for i in range(row - 3):
        for j in range(col - 3):
            if np.sum(matrix[i:i + 4, j:j + 4]) == 42:
                num_of_submatrices += 1
    return num_of_submatrices