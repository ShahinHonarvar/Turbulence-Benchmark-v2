import numpy as np
from itertools import combinations

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row_indices in combinations(range(rows), 121):
        for col_indices in combinations(range(cols), 121):
            submatrix = matrix[np.ix_(row_indices, col_indices)]
            count += 1
    return count