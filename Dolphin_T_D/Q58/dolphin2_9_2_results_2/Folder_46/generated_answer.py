import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    height, width = matrix.shape
    for i in range(height - 11):
        for j in range(width - 12):
            if len(np.unique(matrix[i:i + 12, j:j + 12])) == 144:
                count += 1
    return count