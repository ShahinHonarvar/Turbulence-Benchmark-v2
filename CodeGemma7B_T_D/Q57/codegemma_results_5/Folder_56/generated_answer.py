import numpy as np

def submatrix_with_particular_sum(matrix):
    res = []
    for r1 in range(len(matrix)):
        for r2 in range(r1 + 1, len(matrix) + 1):
            for c1 in range(len(matrix[0])):
                for c2 in range(c1 + 1, len(matrix[0]) + 1):
                    cur = matrix[r1:r2, c1:c2].sum()
                    if cur == -50:
                        res.append(matrix[r1:r2, c1:c2].tolist())
    return res