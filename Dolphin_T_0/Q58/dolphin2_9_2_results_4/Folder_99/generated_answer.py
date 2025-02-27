import numpy as np

def submatrix_with_n_numbers(matrix):
    n = matrix.shape[0]
    num_submatrices = 0
    for i in range(n):
        for j in range(n):
            for k in range(i + 1, n):
                for l in range(j + 1, n):
                    if (k - i + 1) * (l - j + 1) == 146:
                        num_submatrices += 1
    return num_submatrices