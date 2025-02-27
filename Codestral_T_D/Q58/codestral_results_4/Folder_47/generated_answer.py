import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 90
    submatrix_count = 0
    for i in range(rows - int(np.sqrt(n)) + 1):
        for j in range(cols - int(np.sqrt(n)) + 1):
            submatrix = matrix[i:i + int(np.sqrt(n)), j:j + int(np.sqrt(n))]
            if np.sum(submatrix) == 90 and np.prod(submatrix.shape) == n:
                submatrix_count += 1
    return submatrix_count