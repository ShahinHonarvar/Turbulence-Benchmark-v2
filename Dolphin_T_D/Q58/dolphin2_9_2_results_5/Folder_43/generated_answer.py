import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 85
    submatrix_count = 0
    for i in range(len(matrix) - n + 1):
        for j in range(len(matrix[0]) - n + 1):
            if np.all(matrix[i:i + n, j:j + n] == n):
                submatrix_count += 1
    return submatrix_count