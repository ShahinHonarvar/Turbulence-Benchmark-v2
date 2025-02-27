import numpy as np

def submatrix_with_n_numbers(matrix):
    nrows, ncols = matrix.shape
    if nrows < 28 or ncols < 28:
        return 0
    count = 0
    for i in range(nrows - 27):
        for j in range(ncols - 27):
            submatrix = matrix[i:i + 28, j:j + 28]
            if np.all(submatrix == 28):
                count += 1
    return count