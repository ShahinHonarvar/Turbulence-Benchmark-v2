import numpy as np

def submatrix_with_n_numbers(matrix):
    height, width = matrix.shape
    count = 0
    for i in range(height - 11):
        for j in range(width - 11):
            if np.sum(matrix[i:i + 11, j:j + 11]) == 126:
                count += 1
    return count