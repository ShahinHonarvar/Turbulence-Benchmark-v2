import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for top_left in product(range(rows), range(cols)):
        for bottom_right in product(range(top_left[0], rows), range(top_left[1], cols)):
            submatrix = matrix[top_left[0]:bottom_right[0] + 1, top_left[1]:bottom_right[1] + 1]
            if submatrix.sum() == 416:
                submatrices.append(submatrix)
    return submatrices