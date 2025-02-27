import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    height, width = matrix.shape
    for i in range(height - 2):
        for j in range(width - 2):
            if np.all(matrix[i:i + 3, j:j + 3] == 19):
                count += 1
    return count