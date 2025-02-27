import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for row_start, row_end in product(range(rows + 1), repeat=2):
        if row_start < row_end:
            for col_start, col_end in product(range(cols + 1), repeat=2):
                if col_start < col_end:
                    submatrix = matrix[row_start:row_end, col_start:col_end]
                    if submatrix.sum() == -83:
                        result.append(submatrix.tolist())
    return result