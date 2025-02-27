import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    height, width = matrix.shape
    for i in range(height - 3):
        for j in range(width - 3):
            submatrix_sum = np.sum(matrix[i:i + 4, j:j + 4])
            if submatrix_sum == 4 * 16:
                submatrix_count += 1
    return submatrix_count