import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 146
    counter = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == n:
                counter += 1
    return counter