import numpy as np

def submatrix_with_n_numbers(matrix):
    counter = 0
    for ii in range(matrix.shape[0]):
        for jj in range(matrix.shape[1]):
            for ss in range(ii, matrix.shape[0]):
                for tt in range(jj, matrix.shape[1]):
                    length = (ss - ii + 1) * (tt - jj + 1)
                    if length == 180:
                        counter += 1
    return counter