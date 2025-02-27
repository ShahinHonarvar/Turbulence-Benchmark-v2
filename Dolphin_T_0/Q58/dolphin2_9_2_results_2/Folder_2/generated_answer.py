import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_count = 0
    for i in range(rows - 9):
        for j in range(cols - 9):
            if np.sum(matrix[i:i + 10, j:j + 10]) == 107:
                submatrix_count += 1
    return submatrix_count