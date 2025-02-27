import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            submatrix = matrix[i:i + 1, j:j + 1]
            if np.any(np.all(42 == submatrix, axis=1)):
                count += 1
    return count