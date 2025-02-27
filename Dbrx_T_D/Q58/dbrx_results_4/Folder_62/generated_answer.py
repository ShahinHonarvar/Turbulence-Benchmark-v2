import numpy as np

def submatrix_with_n_numbers(matrix):
    nrows, ncols = matrix.shape
    count = 0
    for i in range(nrows - 184):
        for j in range(ncols - 184):
            submatrix = matrix[i:i + 186, j:j + 186]
            if np.isin(submatrix, [186]).all():
                count += 1
    return count