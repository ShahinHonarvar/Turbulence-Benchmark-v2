import numpy as np

def submatrix_with_n_numbers(matrix, n=60):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            if np.sum(matrix[i:i + n, j:j + n]) == 60 * n:
                count += 1
    return count