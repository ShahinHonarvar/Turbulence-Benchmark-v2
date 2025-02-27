import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m - 9):
        for j in range(n - 9):
            if np.count_nonzero(matrix[i:i + 10, j:j + 10]) == 80:
                count += 1
    return count