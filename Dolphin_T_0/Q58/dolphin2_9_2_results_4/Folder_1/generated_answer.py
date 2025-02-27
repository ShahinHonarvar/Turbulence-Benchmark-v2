import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 23
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if i + n <= matrix.shape[0] and j + n <= matrix.shape[1]:
                submatrix = matrix[i:i + n, j:j + n]
                if np.unique(submatrix).size == n:
                    count += 1
    return count