import numpy as np
from itertools import combinations

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r1, c1 in combinations(range(rows), 2):
        for r2, c2 in combinations(range(cols), 2):
            submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
            if submatrix.size == 159 and np.all(submatrix == 159):
                count += 1
    return count