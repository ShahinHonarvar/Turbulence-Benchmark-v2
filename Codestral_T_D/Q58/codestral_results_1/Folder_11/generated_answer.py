import numpy as np

def submatrix_with_n_numbers(matrix, n=38):
    m, n = matrix.shape
    count = 0
    for i in range(m):
        for j in range(n):
            for k in range(i + 1, m + 1):
                for l in range(j + 1, n + 1):
                    if np.sum(matrix[i:k, j:l]) == n:
                        count += 1
    return count