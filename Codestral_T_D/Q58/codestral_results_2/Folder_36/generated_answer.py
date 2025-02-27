import numpy as np

def submatrix_with_n_numbers(matrix):
    height, width = matrix.shape
    count = 0
    for row in range(height - 1):
        for col in range(width - 1):
            submatrix = matrix[row:row + 2, col:col + 2]
            if np.sum(submatrix) == 131 and np.prod(submatrix.shape) == 4:
                count += 1
    return count