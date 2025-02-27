import numpy as np
from itertools import product

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    if rows < 3 or cols < 3:
        return 0
    count = 0
    for r, c in product(range(rows - 2), range(cols - 2)):
        if np.sum(matrix[r:r + 3, c:c + 3]) == 45:
            count += 1
    return count