import numpy as np

def submatrix_with_n_numbers(matrix):
    N = len(matrix)
    M = len(matrix[0])
    count = 0
    for i in range(N - 2):
        for j in range(M - 2):
            if np.count_nonzero(matrix[i:i + 3, j:j + 3]) == 7:
                count += 1
    return count