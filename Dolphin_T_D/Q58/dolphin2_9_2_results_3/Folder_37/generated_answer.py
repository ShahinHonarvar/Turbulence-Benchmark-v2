import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    shape = matrix.shape
    for i in range(shape[0] - 5):
        for j in range(shape[1] - 5):
            sub = matrix[i:i + 6, j:j + 6]
            if np.all(sub == 64):
                count += 1
    return count