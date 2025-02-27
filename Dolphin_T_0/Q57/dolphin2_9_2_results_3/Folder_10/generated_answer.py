import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for r in range(1, min(rows, cols) + 1):
        for comb in combinations(range(rows), 2):
            row_slice = slice(*comb)
            for c in combinations(range(cols), 2):
                col_slice = slice(*c)
                submatrix_sum = np.sum(matrix[row_slice, col_slice])
                if submatrix_sum == 56:
                    submatrices.append(matrix[row_slice, col_slice])
    return submatrices if submatrices else []