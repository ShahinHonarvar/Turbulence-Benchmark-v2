import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    height, width = matrix.shape
    for i in range(height - 7):
        for j in range(width - 7):
            if np.count_nonzero(matrix[i:i + 8, j:j + 8] == 64) == 64:
                count += 1
    return count