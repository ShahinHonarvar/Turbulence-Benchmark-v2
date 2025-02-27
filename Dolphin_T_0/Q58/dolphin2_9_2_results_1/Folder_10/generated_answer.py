import numpy as np

def submatrix_with_n_numbers(matrix):
    n = matrix.shape[0]
    m = matrix.shape[1]
    count = 0
    for i in range(n):
        for j in range(m):
            for x in range(i + 2, n + 1):
                for y in range(j + 2, m + 1):
                    if (x - i + 1) * (y - j + 1) == 56:
                        count += 1
    return count