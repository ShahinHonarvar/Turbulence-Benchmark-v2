import numpy as np

def submatrix_with_n_numbers(matrix):
    mat_shape = matrix.shape
    count = 0
    for i in range(mat_shape[0] - 1):
        for j in range(mat_shape[1] - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if np.isin(submatrix, 66).sum() == 4:
                count += 1
    return count