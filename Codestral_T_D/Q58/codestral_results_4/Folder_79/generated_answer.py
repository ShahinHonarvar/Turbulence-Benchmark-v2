import numpy as np
from itertools import product

def submatrix_with_n_numbers(matrix, n=60):
    rows, cols = matrix.shape
    count = 0
    for r1, c1 in product(range(rows), range(cols)):
        for r2 in range(r1, rows):
            for c2 in range(c1, cols):
                submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                if submatrix.size == n and np.all(submatrix == 60):
                    count += 1
    return count