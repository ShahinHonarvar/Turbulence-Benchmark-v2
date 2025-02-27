import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 146
    rows, cols = matrix.shape
    min_size = int(np.sqrt(n))
    for size in range(min_size, max(rows, cols) + 1):
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if np.prod(submatrix.shape) == n:
                    count += 1
    return count