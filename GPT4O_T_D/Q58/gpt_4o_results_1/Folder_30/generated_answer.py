import numpy as np

def submatrix_with_n_numbers(matrix):
    nrows, ncols = matrix.shape
    if nrows * ncols < 94:
        return 0
    count = 0
    for i in range(nrows):
        for j in range(ncols):
            for p in range(i, nrows):
                for q in range(j, ncols):
                    if (p - i + 1) * (q - j + 1) == 94:
                        count += 1
    return count