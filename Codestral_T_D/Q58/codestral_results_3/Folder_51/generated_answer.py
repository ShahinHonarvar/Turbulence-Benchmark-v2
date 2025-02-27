import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 95
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + n <= rows and j + n <= cols:
                submatrix = matrix[i:i + n, j:j + n]
                if np.sum(submatrix) == n * 95:
                    count += 1
    return count