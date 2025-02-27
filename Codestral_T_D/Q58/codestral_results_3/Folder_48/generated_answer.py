import numpy as np
from itertools import product

def submatrix_with_n_numbers(matrix, n=130):
    rows, cols = matrix.shape
    count = 0
    for r, c in product(range(rows), range(cols)):
        for r_end, c_end in product(range(r, rows), range(c, cols)):
            submatrix = matrix[r:r_end + 1, c:c_end + 1]
            if submatrix.size == n and np.all(submatrix == 130):
                count += 1
    return count