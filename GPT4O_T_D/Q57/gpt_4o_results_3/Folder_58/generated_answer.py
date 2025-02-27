import numpy as np

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    submatrices = []
    for start_row in range(nrows):
        for start_col in range(ncols):
            for end_row in range(start_row, nrows):
                for end_col in range(start_col, ncols):
                    submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                    if np.sum(submatrix) == -137:
                        submatrices.append(submatrix.copy())
    return submatrices