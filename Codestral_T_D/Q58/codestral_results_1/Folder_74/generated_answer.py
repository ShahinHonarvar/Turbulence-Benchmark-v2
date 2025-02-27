import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 48
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 6 + 1):
        for j in range(cols - 6 + 1):
            submatrix = matrix[i:i + 6, j:j + 6]
            if np.sum(submatrix) == n:
                count += 1
    return count