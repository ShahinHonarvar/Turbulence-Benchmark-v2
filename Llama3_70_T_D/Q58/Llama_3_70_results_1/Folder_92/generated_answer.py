import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows - 1):
        for col in range(cols - 1):
            if np.prod(matrix[row:row + 2, col:col + 2].shape) == 8:
                count += 1
            if np.prod(matrix[row:row + 1, col:col + 3].shape) == 8:
                count += 1
            if np.prod(matrix[row:row + 3, col:col + 1].shape) == 8:
                count += 1
            if np.prod(matrix[row:row + 2, col:col + 2].shape) == 16:
                count += 2
            if np.prod(matrix[row:row + 1, col:col + 4].shape) == 8:
                count += 1
            if np.prod(matrix[row:row + 4, col:col + 1].shape) == 8:
                count += 1
    return count