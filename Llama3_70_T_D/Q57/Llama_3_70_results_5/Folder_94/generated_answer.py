import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for row_start, row_end in product(range(rows), range(rows)):
        for col_start, col_end in product(range(cols), range(cols)):
            if row_start <= row_end and col_start <= col_end:
                submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                if np.sum(submatrix) == 92:
                    result.append(submatrix)
    return result