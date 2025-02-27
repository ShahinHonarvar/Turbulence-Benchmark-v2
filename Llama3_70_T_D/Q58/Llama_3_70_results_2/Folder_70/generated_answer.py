import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 173
    m, l = matrix.shape
    count = 0
    for i in range(m):
        for j in range(l):
            for k in range(i, m):
                for end_col in range(j, l):
                    submatrix = matrix[i:k + 1, j:end_col + 1]
                    if submatrix.size == n:
                        count += 1
    return count