import numpy as np

def submatrix_with_n_numbers(matrix):
    height, width = matrix.shape
    count = 0
    for i in range(height - 1):
        for j in range(width - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if submatrix.sum() == 10 * 10:
                count += 1
    return count