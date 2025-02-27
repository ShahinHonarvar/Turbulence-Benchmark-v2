import numpy as np

def submatrix_with_n_numbers(matrix):
    counter = 0
    for row in matrix:
        count = np.count_nonzero(row)
        counter += count
    return counter