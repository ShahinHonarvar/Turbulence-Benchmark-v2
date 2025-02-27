import numpy as np
from itertools import chain

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    all_submatrices = []
    for i in range(rows):
        for j in range(cols):
            for x in chain(range(i, rows), range(i + 1, rows)):
                for y in chain(range(j, cols), range(j + 1, cols)):
                    if np.sum(matrix[i:x + 1, j:y + 1]) == -46:
                        all_submatrices.append(matrix[i:x + 1, j:y + 1])
    return all_submatrices