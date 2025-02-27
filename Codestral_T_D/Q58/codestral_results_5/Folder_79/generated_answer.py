import numpy as np
from itertools import product

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i, j in product(range(rows), range(cols)):
        if i + 9 < rows and j + 9 < cols:
            submatrix = matrix[i:i + 10, j:j + 10]
            if np.sum(submatrix) == 60:
                count += 1
    return count