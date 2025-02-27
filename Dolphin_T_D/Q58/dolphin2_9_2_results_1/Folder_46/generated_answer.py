import numpy as np

def submatrix_with_n_numbers(matrix):
    height, width = matrix.shape
    submatrix_count = 0
    for i in range(height - 11):
        for j in range(width - 11):
            if np.all(matrix[i:i + 12, j:j + 12] == 144):
                submatrix_count += 1
    return submatrix_count