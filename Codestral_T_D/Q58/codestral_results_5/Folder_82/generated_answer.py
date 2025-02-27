import numpy as np

def submatrix_with_n_numbers(matrix):
    n, m = matrix.shape
    count = 0
    for i in range(n):
        for j in range(m):
            for k in range(i + 1, n + 1):
                for l in range(j + 1, m + 1):
                    if np.count_nonzero(matrix[i:k, j:l] == 99) == (k - i) * (l - j):
                        count += 1
    return count