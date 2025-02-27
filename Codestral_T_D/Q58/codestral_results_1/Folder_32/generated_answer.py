import numpy as np

def submatrix_with_n_numbers(matrix, n=103):
    row, col = matrix.shape
    count = 0
    for i in range(row):
        for j in range(col):
            for k in range(i, row):
                for l in range(j, col):
                    if (k - i + 1) * (l - j + 1) == n:
                        count += 1
    return count