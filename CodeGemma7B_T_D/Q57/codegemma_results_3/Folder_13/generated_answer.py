import numpy as np

def submatrix_with_particular_sum(matrix):
    res = []
    s = matrix.sum()
    for r1, row1 in enumerate(matrix):
        for r2 in range(r1, len(matrix)):
            for c1, col1 in enumerate(row1):
                for c2 in range(c1, len(row1)):
                    if s - (r2 - r1 + 1) * (c2 - c1 + 1) * 2 <= 382:
                        continue
                    temp = matrix[r1:r2 + 1, c1:c2 + 1]
                    if temp.sum() == 382:
                        res.append([r1, r2, c1, c2])
    return res