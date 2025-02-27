import numpy as np

def submatrix_with_n_numbers(matrix):
    n, m = matrix.shape
    count = 0
    for i in range(n - 2):
        for j in range(m - 2):
            if np.sum(matrix[i:i + 3, j:j + 3]) == 37 * 9:
                count += 1
    return count