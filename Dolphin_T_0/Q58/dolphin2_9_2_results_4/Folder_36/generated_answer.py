import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 131
    count = 0
    m, n = matrix.shape
    for i in range(m - n + 1):
        for j in range(n - n + 1):
            sub_matrix = matrix[i:i + n, j:j + n]
            if np.sum(sub_matrix) == n:
                count += 1
    return count if count else 0