import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 43
    shape = matrix.shape
    count = 0
    for i in range(shape[0]):
        for j in range(shape[1]):
            for k in range(i + 1, shape[0] + 1):
                for l in range(j + 1, shape[1] + 1):
                    if np.sum(matrix[i:k, j:l]) == n:
                        count += 1
    return count