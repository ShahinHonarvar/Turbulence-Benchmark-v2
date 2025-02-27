import numpy as np

def submatrix_with_n_numbers(matrix):
    n, m = matrix.shape
    count = 0
    for i in range(n - 1):
        for j in range(m - 1):
            sub_matrix = matrix[i:i + 1, j:j + 1]
            if np.any(np.all(sub_matrix == 144, axis=1)):
                count += 1
    return count