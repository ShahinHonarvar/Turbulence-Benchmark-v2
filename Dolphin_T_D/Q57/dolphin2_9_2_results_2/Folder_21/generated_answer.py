import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):
    matrix = np.array(matrix)
    sub_matrices = sum([list(combinations(matrix, i)) for i in range(1, matrix.shape[0] + 1)], [])
    sub_matrices_with_sum_equal_minus936 = [sub_matrix for sub_matrix in sub_matrices if np.sum(sub_matrix) == -936]
    if sub_matrices_with_sum_equal_minus936:
        return sub_matrices_with_sum_equal_minus936
    else:
        return []