import numpy as np
from itertools import product

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r, c in product(range(rows - 2), range(cols - 2)):
        if len(set(matrix[r:r + 3, c:c + 3].flatten())) == 7:
            count += 1
    return count