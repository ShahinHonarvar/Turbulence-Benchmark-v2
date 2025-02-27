import numpy as np

def submatrix_with_n_numbers(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    n = 126
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            if np.count_nonzero(matrix[i:i + n, j:j + n]) == n:
                count += 1
    return count