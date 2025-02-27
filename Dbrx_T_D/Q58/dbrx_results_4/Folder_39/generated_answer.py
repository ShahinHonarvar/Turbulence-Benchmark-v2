import numpy as np

def submatrix_with_n_numbers(matrix):
    height, width = matrix.shape
    total_submatrices = height * width
    count = 0
    for i in range(height):
        for j in range(width):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.isin(submatrix, np.array([59])).sum() == 9:
                count += 1
    return count if count > 0 else 0