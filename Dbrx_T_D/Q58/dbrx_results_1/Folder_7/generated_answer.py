import numpy as np

def submatrix_with_n_numbers(matrix):
    nrows, ncols = matrix.shape
    count = 0
    for i in range(nrows - 2):
        for j in range(ncols - 4):
            submatrix = matrix[i:i + 3, j:j + 5]
            if np.isin(121, submatrix).any():
                count += 1
    return count