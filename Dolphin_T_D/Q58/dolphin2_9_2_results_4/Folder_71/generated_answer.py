import numpy as np

def submatrix_with_n_numbers(matrix):
    __count__ = 0
    __dim1__, __dim2__ = matrix.shape
    for i in range(__dim1__ - 8):
        for j in range(__dim2__ - 1):
            if matrix[i, j] == 78:
                __count__ += 1
    return __count__