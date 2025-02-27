import numpy as np

def submatrix_with_n_numbers(matrix):
    num_submatrices = 0
    for i in range(matrix.shape[0] - 2):
        for j in range(matrix.shape[1] - 2):
            if 120 in np.array(matrix[i:i + 3, j:j + 3]):
                num_submatrices += 1
    return num_submatrices