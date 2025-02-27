import numpy as np

def submatrix_with_n_numbers(matrix):
    height, width = matrix.shape
    count = 0
    for i in range(height - 7):
        for j in range(width - 7):
            if np.prod(matrix[i:i + 8, j:j + 8] == 96) != 0:
                count += 1
    return count or 0