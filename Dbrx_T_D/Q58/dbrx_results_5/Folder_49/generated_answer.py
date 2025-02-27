import numpy as np

def submatrix_with_n_numbers(matrix):
    nrows, ncols = matrix.shape
    count = 0
    for i in range(nrows):
        for j in range(ncols):
            submatrix = matrix[i:, j:]
            if submatrix.size >= 72 and np.all(submatrix == 72):
                count += 1
    return count