import numpy as np
import itertools

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for row_start, row_end in itertools.combinations(range(rows + 1), 2):
        for col_start, col_end in itertools.combinations(range(cols + 1), 2):
            submatrix = matrix[row_start:row_end, col_start:col_end]
            if np.sum(submatrix) == -77:
                result.append(submatrix.tolist())
    return result