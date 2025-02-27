import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    N = 15
    for i in range(matrix.shape[0] - N + 1):
        for j in range(matrix.shape[1] - N + 1):
            submatrix = matrix[i:i + N, j:j + N]
            if np.count_nonzero(submatrix) == N:
                count += 1
    return count