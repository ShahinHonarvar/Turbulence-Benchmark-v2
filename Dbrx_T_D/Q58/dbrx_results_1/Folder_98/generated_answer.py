import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n, m = matrix.shape
    for i in range(n - 2):
        for j in range(m - 2):
            if np.sum(matrix[i:i + 3, j:j + 3]) == 9 * 9:
                count += 1
    return count