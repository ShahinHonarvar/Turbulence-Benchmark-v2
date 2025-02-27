import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrices = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    if (k - i + 1) * (l - j + 1) == 93:
                        submatrices += 1
    return submatrices