import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    counter = 0
    for i in range(m):
        for j in range(n):
            if i + 3 < m and j + 4 < n and (sum(matrix[i:i + 4, j:j + 4].flatten()) == 80):
                counter += 1
    return counter