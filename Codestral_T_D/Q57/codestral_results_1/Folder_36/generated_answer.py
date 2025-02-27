import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for top_left, bottom_right in product(range(rows), repeat=2):
        for i in range(top_left, bottom_right + 1):
            for j in range(top_left, bottom_right + 1):
                submatrix = matrix[i:bottom_right + 1, j:bottom_right + 1]
                if np.sum(submatrix) == -779:
                    submatrices.append(submatrix)
    return submatrices