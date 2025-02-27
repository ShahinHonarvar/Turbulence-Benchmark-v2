import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 39
    nrows, ncols = matrix.shape
    count = 0
    for i in range(nrows - n + 1):
        for j in range(ncols - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.all(submatrix == 39):
                count += 1
    return count