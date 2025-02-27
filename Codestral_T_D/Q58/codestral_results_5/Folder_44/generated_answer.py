import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 191
    rows, cols = matrix.shape
    total = 0
    for i in range(rows):
        for j in range(cols):
            if i + n - 1 < rows and j + n - 1 < cols:
                submatrix = matrix[i:i + n, j:j + n]
                if np.sum(submatrix) == n * 191:
                    total += 1
    return total