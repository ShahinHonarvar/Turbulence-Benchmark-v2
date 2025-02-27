import numpy as np
from itertools import combinations

def submatrix_with_n_numbers(matrix):
    n = 18
    m, k = matrix.shape
    count = 0
    for i in range(m - n + 1):
        for j in range(k - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if len(np.unique(submatrix)) == n:
                count += 1
    return count