import numpy as np

def submatrix_with_n_numbers(matrix):
    row, col = matrix.shape
    count = 0
    n = 139
    for i in range(row - n + 1):
        for j in range(col - n + 1):
            if np.count_nonzero(matrix[i:i + n, j:j + n]) == n:
                count += 1
    return count