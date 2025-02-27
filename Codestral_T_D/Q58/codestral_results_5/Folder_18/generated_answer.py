import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 104
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + n - 1 < rows and j + n - 1 < cols:
                submatrix = matrix[i:i + n, j:j + n]
                if np.prod(submatrix.shape) == n:
                    count += 1
    return count