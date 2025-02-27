import numpy as np
from itertools import product

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i, j in product(range(rows - 1), range(cols - 1)):
        if matrix[i:i + 2, j:j + 2].size == 8:
            count += 1
    return count