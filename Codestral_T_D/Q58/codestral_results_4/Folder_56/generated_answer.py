import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 68
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + n - 1 < rows and j + n - 1 < cols:
                if np.sum(matrix[i:i + n, j:j + n]) == 68 * matrix[i, j]:
                    count += 1
    return count