import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            sub_matrices = list(combinations(matrix, r))
            for sub_matrix in sub_matrices:
                if np.sum(sub_matrix) == 901:
                    result.append(sub_matrix)
    return result