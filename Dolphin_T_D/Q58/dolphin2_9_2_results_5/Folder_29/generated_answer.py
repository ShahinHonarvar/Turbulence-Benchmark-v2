import numpy as np

def submatrix_with_n_numbers(matrix):
    n = len(matrix)
    m = len(matrix[0])
    count = 0
    for i in range(n - 1):
        for j in range(m - 1):
            if 19 in matrix[i:i + 2, j:j + 2]:
                count += 1
    return count