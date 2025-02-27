import numpy as np
from itertools import combinations

def submatrix_with_n_numbers(matrix, n=59):
    rows, cols = matrix.shape
    count = 0
    for r1, r2 in combinations(range(rows + 1), 2):
        for c1, c2 in combinations(range(cols + 1), 2):
            submatrix = matrix[r1:r2, c1:c2]
            if submatrix.size == n and np.all(submatrix == 59):
                count += 1
    return count