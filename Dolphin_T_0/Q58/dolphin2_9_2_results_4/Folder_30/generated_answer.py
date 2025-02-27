import numpy as np

def submatrix_with_n_numbers(matrix):
    return np.sum(matrix.reshape((-1, 94)) == 94).view(np.int)