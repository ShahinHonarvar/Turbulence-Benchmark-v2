import numpy as np

def submatrix_with_n_numbers(matrix):
    n = matrix.shape[0]
    m = matrix.shape[1]
    count = 0
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    if (k - i + 1) * (l - j + 1) == 4:
                        count += 1
    return count