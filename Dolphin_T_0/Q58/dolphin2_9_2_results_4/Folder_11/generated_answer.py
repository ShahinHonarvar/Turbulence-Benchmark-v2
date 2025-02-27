import numpy as np

def submatrix_with_n_numbers(matrix, n=38):
    shape = matrix.shape
    submatrix_count = 0
    for i in range(shape[0]):
        for j in range(shape[1]):
            for k in range(shape[0] - i):
                for l in range(shape[1] - j):
                    if np.sum(matrix[i:i + k + 1, j:j + l + 1]) == n:
                        submatrix_count += 1
    return submatrix_count