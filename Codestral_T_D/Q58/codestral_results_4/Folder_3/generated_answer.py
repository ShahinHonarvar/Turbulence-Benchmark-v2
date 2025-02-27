import numpy as np

def submatrix_with_n_numbers(matrix, n=54):
    r, c = matrix.shape
    count = 0
    for i in range(r):
        for j in range(c):
            for k in range(i + 1, r + 1):
                for l in range(j + 1, c + 1):
                    if (k - i) * (l - j) == n:
                        count += 1
    return count