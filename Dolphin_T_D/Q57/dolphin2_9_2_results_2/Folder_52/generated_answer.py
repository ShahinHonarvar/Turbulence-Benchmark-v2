import numpy as np
from itertools import combinations

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    sub_matrices = []
    all_subsets_of_indices = [*combinations(range(m), 2), *combinations(range(n), 2)]
    for i, j in all_subsets_of_indices:
        if i < j:
            for k, l in combinations(range(j - i), 2):
                submatrix = matrix[i:j, k:l]
                if np.sum(submatrix) == 100:
                    sub_matrices.append(submatrix.tolist())
    return sub_matrices