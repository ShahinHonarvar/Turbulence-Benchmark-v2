import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for top_left, bottom_right in product(range(rows), repeat=2):
        for row in range(top_left, bottom_right + 1):
            for col in range(top_left, bottom_right + 1):
                if np.sum(matrix[top_left:bottom_right + 1, top_left:bottom_right + 1]) == -59:
                    submatrices.append(matrix[top_left:bottom_right + 1, top_left:bottom_right + 1])
    return submatrices