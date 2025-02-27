import numpy as np

def submatrix_with_n_numbers(matrix):
    total_submatrices = 0
    for i in range(matrix.shape[0] - 4):
        for j in range(matrix.shape[1] - 4):
            submatrix = matrix[i:i + 5, j:j + 5]
            if len(np.unique(submatrix)) == 48:
                total_submatrices += 1
    return total_submatrices