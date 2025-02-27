import numpy as np
from itertools import product

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 99
    rows, cols = matrix.shape
    for size in range(1, min(rows, cols) + 1):
        for row in range(rows - size + 1):
            for col in range(cols - size + 1):
                submatrix = matrix[row:row + size, col:col + size]
                if np.sum(submatrix) == sum(range(1, n + 1)):
                    count += 1
    return count