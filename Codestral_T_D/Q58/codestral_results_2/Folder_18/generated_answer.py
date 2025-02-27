import numpy as np
from itertools import combinations

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r1, r2 in combinations(range(rows + 1), 2):
        for c1, c2 in combinations(range(cols + 1), 2):
            if np.sum(matrix[r1:r2, c1:c2]) == 104:
                count += 1
    return count