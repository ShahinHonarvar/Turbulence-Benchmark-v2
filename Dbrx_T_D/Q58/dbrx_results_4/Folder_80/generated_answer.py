import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrices_with_180 = 0
    for i in range(matrix.shape[0] - 17):
        for j in range(matrix.shape[1] - 17):
            submatrix = matrix[i:i + 18, j:j + 18]
            if np.sum(submatrix) == 180:
                submatrices_with_180 += 1
    return submatrices_with_180