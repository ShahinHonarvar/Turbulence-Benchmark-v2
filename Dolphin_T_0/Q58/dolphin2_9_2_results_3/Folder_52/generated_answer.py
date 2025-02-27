import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    counter = 0
    for i in range(m):
        for j in range(n):
            for k in range(i + 1, m):
                for l in range(j + 1, n):
                    if np.sum(matrix[i:k, j:l + 1]) == 147:
                        counter += 1
    return counter