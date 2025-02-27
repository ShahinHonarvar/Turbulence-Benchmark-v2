import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 185
    size = len(matrix[0])
    for i in range(len(matrix)):
        for j in range(size):
            if sum(matrix[i][j:j + size]) == n:
                count += 1
    return count