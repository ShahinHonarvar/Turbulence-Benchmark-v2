import numpy as np
import itertools

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for size in range(1, min(rows, cols) + 1):
        for row in range(rows - size + 1):
            for col in range(cols - size + 1):
                submatrix = matrix[row:row + size, col:col + size]
                if np.prod(submatrix.shape) == 59 and np.all(submatrix >= 0):
                    count += 1
    return count