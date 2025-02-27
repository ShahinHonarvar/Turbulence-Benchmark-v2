import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    nrows, ncols = matrix.shape
    for i in range(nrows - 2 + 1):
        for j in range(ncols - 2 + 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if submatrix.sum() == 18:
                count += 1
    return count