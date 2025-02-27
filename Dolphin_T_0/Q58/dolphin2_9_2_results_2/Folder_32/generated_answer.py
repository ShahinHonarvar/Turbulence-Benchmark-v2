import numpy as np

def submatrix_with_n_numbers(matrix):
    M, N = matrix.shape
    count = 0
    for i in range(M - 2):
        for j in range(N - 2):
            if np.sum(matrix[i:i + 3, j:j + 3]) == 103:
                count += 1
    return count