import numpy as np

def submatrix_with_n_numbers(matrix):
    height, width = matrix.shape
    count = 0
    for i in range(height - 2):
        for j in range(width - 2):
            if np.sum(matrix[i:i + 3, j:j + 3]) == 42:
                count += 1
    return count