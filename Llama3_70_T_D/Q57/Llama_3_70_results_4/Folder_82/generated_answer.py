import itertools
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for row_start, row_end in itertools.combinations(range(rows + 1), 2):
        for col_start, col_end in itertools.combinations(range(cols + 1), 2):
            submatrix = matrix[row_start:row_end, col_start:col_end]
            if np.sum(submatrix) == -27:
                result.append(submatrix)
    return result