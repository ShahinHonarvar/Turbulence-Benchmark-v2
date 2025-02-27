import numpy as np

def submatrix_with_n_numbers(matrix):
    height, width = matrix.shape
    count = 0
    for i in range(height - 3):
        for j in range(width - 3):
            submatrix = matrix[i:i + 4, j:j + 4]
            if submatrix.sum() == 80 * 4 * 4:
                count += 1
    return count