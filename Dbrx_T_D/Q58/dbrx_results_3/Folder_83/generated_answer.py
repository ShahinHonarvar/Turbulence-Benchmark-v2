import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 46):
        for j in range(matrix.shape[1] - 46):
            submatrix = matrix[i:i + 47, j:j + 47]
            if np.isin(submatrix, 47).all():
                count += 1
    return count