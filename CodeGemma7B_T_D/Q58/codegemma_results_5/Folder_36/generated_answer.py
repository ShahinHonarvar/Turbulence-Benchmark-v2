import numpy as np

def submatrix_with_n_numbers(matrix):
    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(i + 1, len(matrix)):
                for l in range(j + 1, len(matrix)):
                    if len(set(matrix[i][j:l + 1].flatten())) == 131 and len(set(matrix[i:k + 1][j].flatten())) == 131:
                        res += 1
    return res