import numpy as np

def submatrix_with_n_numbers(matrix):
    n = len(matrix)
    count = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 27:
                count += 1
    return count