import numpy as np
from itertools import combinations

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i, j in combinations(range(m + 1), 2):
        for k, l in combinations(range(n + 1), 2):
            submatrix = matrix[i:j, k:l]
            if submatrix.size == 77 and np.all(submatrix == 77):
                count += 1
    return count