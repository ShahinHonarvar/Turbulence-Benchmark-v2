import numpy as np
from itertools import combinations

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 46
    for row_comb in combinations(range(rows), n):
        for col_comb in combinations(range(cols), n):
            submatrix = matrix[np.ix_(row_comb, col_comb)]
            if submatrix.size == n:
                count += 1
    return count