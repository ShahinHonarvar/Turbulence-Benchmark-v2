import numpy as np

def submatrix_with_particular_sum(matrix):
    return np.where(np.sum(matrix, axis=1) == 59, matrix, np.empty(0))