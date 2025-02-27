import numpy as np

def submatrix_with_n_numbers(matrix, n=64):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - np.sqrt(n) + 1):
        for j in range(cols - np.sqrt(n) + 1):
            if np.prod(matrix[i:i + int(np.sqrt(n)), j:j + int(np.sqrt(n))].shape) == n:
                count += 1
    return count