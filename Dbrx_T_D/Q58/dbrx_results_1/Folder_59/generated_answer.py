import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrices_with_n_numbers = 0
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if np.isin(submatrix, 76).sum() == 4:
                submatrices_with_n_numbers += 1
    return submatrices_with_n_numbers