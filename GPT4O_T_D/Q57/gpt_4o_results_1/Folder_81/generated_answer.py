import numpy as np

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    result = []
    for row_start in range(nrows):
        for row_end in range(row_start, nrows):
            for col_start in range(ncols):
                for col_end in range(col_start, ncols):
                    submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                    if np.sum(submatrix) == -90:
                        result.append(submatrix)
    return result