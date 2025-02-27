import numpy as np
from itertools import product

def submatrix_with_n_numbers(matrix, n=16):
    rows, cols = matrix.shape
    count = 0
    for r, c in product(range(rows - 3), range(cols - 3)):
        submatrix = matrix[r:r + 4, c:c + 4]
        if submatrix.size == n and np.all(submatrix >= 0):
            count += 1
    return count