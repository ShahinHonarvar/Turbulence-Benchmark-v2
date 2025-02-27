import numpy as np

def submatrix_with_n_numbers(matrix):
    num_submatrices = 0
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if np.isin(submatrix, 144).all():
                num_submatrices += 1
    return num_submatrices