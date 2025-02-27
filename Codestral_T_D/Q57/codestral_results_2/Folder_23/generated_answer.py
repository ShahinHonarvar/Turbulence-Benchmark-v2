import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for row1, row2 in combinations(range(matrix.shape[0] + 1), 2):
        for col1, col2 in combinations(range(matrix.shape[1] + 1), 2):
            submatrix = matrix[row1:row2, col1:col2]
            if submatrix.sum() == 59:
                submatrices.append(submatrix)
    return submatrices