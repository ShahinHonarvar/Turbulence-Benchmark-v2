import numpy as np
from itertools import combinations

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for r2, c2 in combinations(range(r, rows), 2):
                for c3, c4 in combinations(range(c, cols), 2):
                    submatrix = matrix[r:r2 + 1, c:c4 + 1]
                    if len(submatrix.flatten()) == 2:
                        count += 1
                    elif len(submatrix.flatten()) > 2:
                        for s1, s2 in combinations(range(len(submatrix.flatten())), 2):
                            count += 1
    return count