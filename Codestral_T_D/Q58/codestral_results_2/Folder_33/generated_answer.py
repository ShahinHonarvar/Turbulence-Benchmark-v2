import numpy as np

def submatrix_with_n_numbers(matrix, n=118):
    m, n = matrix.shape
    count = 0
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    if np.sum(matrix[i:k + 1, j:l + 1]) == n:
                        count += 1
    return count