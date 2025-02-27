import numpy as np
from collections import Counter

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m):
        for j in range(n):
            for p in range(i + 1, m + 1):
                for q in range(j + 1, n + 1):
                    submatrix = matrix[i:p, j:q]
                    if Counter(submatrix.flatten())[37] == 37:
                        count += 1
    return count