import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 103
    submatrix_count = 0
    for i in range(len(matrix) - n + 1):
        for j in range(len(matrix[0]) - n + 1):
            if np.sum(matrix[i:i + n, j:j + n]) == int(n * n * (n + 1) / 2):
                submatrix_count += 1
    return submatrix_count