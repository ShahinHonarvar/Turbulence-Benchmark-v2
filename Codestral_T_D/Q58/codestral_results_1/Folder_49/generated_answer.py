import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 72
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - int(np.sqrt(n)) + 1):
        for j in range(cols - int(np.sqrt(n)) + 1):
            if np.sum(matrix[i:i + int(np.sqrt(n)), j:j + int(np.sqrt(n))]) == n * matrix[i, j]:
                count += 1
    return count