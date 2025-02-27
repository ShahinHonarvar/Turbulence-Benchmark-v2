import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 154
    shape = matrix.shape
    count = 0
    for i in range(shape[0] - n + 1):
        for j in range(shape[1] - n + 1):
            sub_matrix = matrix[i:i + n, j:j + n]
            if np.sum(sub_matrix) == n * n:
                count += 1
    return count