import numpy as np
from itertools import combinations

def submatrix_with_n_numbers(matrix, n=56):
    row, col = matrix.shape
    count = 0
    for r in range(1, row + 1):
        for c in range(1, col + 1):
            for sub_rows in combinations(range(row), r):
                for sub_cols in combinations(range(col), c):
                    if np.sum(matrix[np.ix_(sub_rows, sub_cols)]) == n:
                        count += 1
    return count