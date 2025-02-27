import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 147
    submatrix_count = 0
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            if np.count_nonzero(matrix[i:i + n, j:j + n]) == n:
                submatrix_count += 1
    return submatrix_count