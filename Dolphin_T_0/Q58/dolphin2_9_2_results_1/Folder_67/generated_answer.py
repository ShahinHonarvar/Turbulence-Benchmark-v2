import numpy as np

def submatrix_with_n_numbers(matrix):
    shape = matrix.shape
    submatrices = 0
    for i in range(shape[0]):
        for j in range(shape[1]):
            for k in range(shape[0], 100):
                if k - i < 43:
                    break
                for l in range(shape[1], 100):
                    if l - j < 43:
                        break
                    if np.count_nonzero(matrix[i:k, j:l]) == 43:
                        submatrices += 1
    return submatrices