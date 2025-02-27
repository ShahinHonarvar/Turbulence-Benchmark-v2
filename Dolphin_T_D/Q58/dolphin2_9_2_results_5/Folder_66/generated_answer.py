import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    shape = matrix.shape
    for i in range(shape[0] - 2):
        for j in range(shape[1] - 2):
            if np.count_nonzero(matrix[i:i + 3, j:j + 3]) == 42:
                count += 1
    return count