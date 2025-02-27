import numpy as np

def submatrix_with_n_numbers(matrix):
    M = len(matrix)
    N = len(matrix[0])
    counter = 0
    for i in range(M - 1):
        for j in range(N - 1):
            if matrix[i][j] == 41 and matrix[i + 1][j + 1] == 41:
                if matrix[i][j + 1] == 41 and matrix[i + 1][j] == 41:
                    counter += 1
    return counter