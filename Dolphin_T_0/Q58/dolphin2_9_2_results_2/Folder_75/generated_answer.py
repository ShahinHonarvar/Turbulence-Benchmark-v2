import numpy as np

def submatrix_with_n_numbers(matrix):
    shape = matrix.shape
    height = shape[0]
    width = shape[1]
    count = 0
    for i in range(height - 7):
        for j in range(width - 3):
            submatrix = matrix[i:i + 8, j:j + 3]
            if np.sum(submatrix) == 80:
                count += 1
    return count