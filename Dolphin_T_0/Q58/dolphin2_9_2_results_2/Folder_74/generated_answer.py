import numpy as np

def submatrix_with_n_numbers(matrix):
    n = len(matrix[0])
    m = len(matrix)
    submatrixes = 0
    for i in range(m):
        for j in range(n):
            for k in range(i + 1, m):
                for l in range(j + 1, n):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if len(submatrix) == 48:
                        submatrixes += 1
    return submatrixes