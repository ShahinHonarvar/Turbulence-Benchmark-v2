import numpy as np

def submatrix_with_n_numbers(matrix):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i + 1, matrix.shape[0] + 1):
                for l in range(j + 1, matrix.shape[1] + 1):
                    if np.sum(matrix[i:k, j:l]) == 68:
                        return 1
    return 0