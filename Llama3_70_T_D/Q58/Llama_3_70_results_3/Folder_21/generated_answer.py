import numpy as np
import itertools

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for r2 in range(r + 1, rows + 1):
                for c2 in range(c + 1, cols + 1):
                    submatrix = matrix[r:r2, c:c2]
                    if np.prod(submatrix.shape) == 139 and np.sum(submatrix) == 139 * submatrix[0, 0]:
                        count += 1
    return count