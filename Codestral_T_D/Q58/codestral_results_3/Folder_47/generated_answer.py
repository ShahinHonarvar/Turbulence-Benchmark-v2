import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 90
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + int(np.sqrt(n)) - 1 < rows and j + int(np.sqrt(n)) - 1 < cols:
                submatrix = matrix[i:i + int(np.sqrt(n)), j:j + int(np.sqrt(n))]
                if np.prod(submatrix.shape) == n:
                    count += 1
    return count