import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 121
    height, width = matrix.shape
    count = 0
    for i in range(height - 2):
        for j in range(width - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.sum(submatrix) == n:
                count += 1
    return count