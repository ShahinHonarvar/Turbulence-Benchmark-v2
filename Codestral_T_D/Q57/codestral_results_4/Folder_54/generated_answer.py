import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for top_left, bottom_right in product(range(rows), repeat=2):
        for i in range(top_left, bottom_right + 1):
            for j in range(top_left, bottom_right + 1):
                submatrix = matrix[top_left:i + 1, top_left:j + 1]
                if np.sum(submatrix) == -59:
                    submatrices.append(submatrix)
    return submatrices