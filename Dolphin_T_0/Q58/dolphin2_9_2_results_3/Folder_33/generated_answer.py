import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    cnt = 0
    for i in range(m):
        for j in range(n):
            for x in range(i + 1, m + 1):
                for y in range(j + 1, n + 1):
                    submatrix = matrix[i:x, j:y]
                    if len(submatrix.flatten()) == 118:
                        cnt += 1
    return cnt