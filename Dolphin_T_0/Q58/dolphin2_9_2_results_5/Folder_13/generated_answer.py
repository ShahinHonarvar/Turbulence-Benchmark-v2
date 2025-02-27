import numpy as np

def submatrix_with_n_numbers(matrix):
    height, width = matrix.shape
    count = 0
    for i in range(height - 21 + 1):
        for j in range(width - 21 + 1):
            if np.sum(matrix[i:i + 22, j:j + 22]) == 175:
                count += 1
    return count