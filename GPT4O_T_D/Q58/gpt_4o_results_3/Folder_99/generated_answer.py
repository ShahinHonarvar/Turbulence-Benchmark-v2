import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 146
    m, p = matrix.shape
    count = 0
    for i in range(m):
        for j in range(p):
            for x in range(i, m):
                for y in range(j, p):
                    submatrix = matrix[i:x + 1, j:y + 1]
                    if submatrix.size == n:
                        count += 1
    return count