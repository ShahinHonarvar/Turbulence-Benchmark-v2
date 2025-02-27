import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 67
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    if np.count_nonzero(matrix[i:k, j:l]) == n:
                        count += 1
    return count