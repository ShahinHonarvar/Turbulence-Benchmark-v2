import numpy as np

def submatrix_with_n_numbers(matrix):
    n = len(matrix)
    m = len(matrix[0])
    counter = 0
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    if len(matrix[i:k + 1, j:l + 1].flatten()) == 37:
                        counter += 1
    return counter