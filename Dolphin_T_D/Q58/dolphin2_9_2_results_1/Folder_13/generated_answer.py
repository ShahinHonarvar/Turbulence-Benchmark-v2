import numpy as np

def submatrix_with_n_numbers(matrix):
    N = 175
    rows, cols = matrix.shape
    submatrices = 0
    for i in range(rows - N + 1):
        for j in range(cols - N + 1):
            count = np.count_nonzero(matrix[i:i + N, j:j + N] == N)
            if count == N:
                submatrices += 1
    return submatrices