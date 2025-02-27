import numpy as np

def submatrix_with_n_numbers(matrix):
    num_submatrices = 0
    for i in range(matrix.shape[0] - 9):
        for j in range(matrix.shape[1] - 9):
            substr = matrix[i:i + 10, j:j + 10]
            if np.count_nonzero(substr == 85) == 85:
                num_submatrices += 1
    return num_submatrices