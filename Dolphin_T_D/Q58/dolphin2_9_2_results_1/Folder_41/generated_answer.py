import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i, j] == 73:
                count += 1
    return count