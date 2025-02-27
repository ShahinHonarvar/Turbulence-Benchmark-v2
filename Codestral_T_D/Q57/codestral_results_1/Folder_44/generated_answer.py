import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for top, bottom, left, right in product(range(rows), repeat=4):
        if top <= bottom and left <= right:
            submatrix = matrix[top:bottom + 1, left:right + 1]
            if submatrix.sum() == 830:
                result.append(submatrix)
    return result