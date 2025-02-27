import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    height, width = matrix.shape
    target_sum = 35
    for r1, c1, r2, c2 in product(range(height), repeat=4):
        if r2 >= r1 and c2 >= c1:
            submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
            if submatrix.sum() == target_sum:
                return submatrix
    return []