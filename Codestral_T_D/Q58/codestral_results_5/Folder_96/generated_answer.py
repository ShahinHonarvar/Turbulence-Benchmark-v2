import numpy as np
from itertools import combinations

def submatrix_with_n_numbers(matrix):

    def is_submatrix(submatrix):
        return np.prod(submatrix.shape) == 20

    def get_submatrices(matrix):
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                for k in range(i, matrix.shape[0]):
                    for l in range(j, matrix.shape[1]):
                        yield matrix[i:k + 1, j:l + 1]
    return sum((is_submatrix(submatrix) for submatrix in get_submatrices(matrix)))