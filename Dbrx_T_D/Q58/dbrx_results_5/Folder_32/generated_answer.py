import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n_submatrix = np.full((3, 3), 103)
    for i in range(matrix.shape[0] - 2):
        for j in range(matrix.shape[1] - 2):
            if np.all(matrix[i:i + 3, j:j + 3] == n_submatrix):
                count += 1
    return count