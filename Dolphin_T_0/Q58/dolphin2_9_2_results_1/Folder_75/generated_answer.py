import numpy as np

def submatrix_with_n_numbers(matrix):
    index = np.arange(matrix.shape[0])
    count = 0
    for i in range(1, matrix.shape[0] + 1):
        for j in range(1, matrix.shape[1] + 1):
            if i * j == 80:
                count += 1
    return count