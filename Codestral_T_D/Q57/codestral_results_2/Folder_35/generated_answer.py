import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for start_row, end_row in product(range(rows), repeat=2):
        for start_col, end_col in product(range(cols), repeat=2):
            submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
            if submatrix.sum() == 432:
                result.append(submatrix)
    return result