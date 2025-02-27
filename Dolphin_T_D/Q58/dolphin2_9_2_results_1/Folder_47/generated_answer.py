import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 10):
        for j in range(matrix.shape[1] - 10):
            if np.all(matrix[i:i + 10, j:j + 10] == 90):
                count += 1
    return count