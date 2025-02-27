import numpy as np

def submatrix_with_n_numbers(matrix):
    if np.size(matrix) < 121:
        return 0
    count = 0
    for i in range(matrix.shape[0] - 10):
        for j in range(matrix.shape[1] - 10):
            if np.all(matrix[i:i + 11, j:j + 11] == 121):
                count += 1
    return count