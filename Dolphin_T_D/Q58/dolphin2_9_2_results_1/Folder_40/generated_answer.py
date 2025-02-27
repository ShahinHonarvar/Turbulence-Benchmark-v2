import numpy as np

def submatrix_with_n_numbers(matrix):
    row = len(matrix)
    col = len(matrix[0])
    res = 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1:
                for k in range(i, row):
                    for l in range(j, col):
                        if (k - i + 1) * (l - j + 1) == 1:
                            res += 1
    return res