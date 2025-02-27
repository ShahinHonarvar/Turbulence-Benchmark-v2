import numpy as np

def submatrix_with_n_numbers(matrix):
    M, N = matrix.shape
    count = 0
    for i in range(M):
        for j in range(N):
            if matrix[i, j] == 18:
                if i > 0 and matrix[i - 1, j] >= 0 and (matrix[i - 1, j] <= 18) and (j > 0) and (matrix[i, j - 1] >= 0) and (matrix[i, j - 1] <= 18):
                    matrix[i, j] = -1
                    count += 1
    return count