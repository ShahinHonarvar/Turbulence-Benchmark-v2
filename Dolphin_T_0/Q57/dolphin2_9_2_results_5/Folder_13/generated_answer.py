import numpy as np

def submatrix_with_particular_sum(matrix):
    h, w = matrix.shape
    sum_matrix = matrix.cumsum(axis=0).cumsum(axis=1)
    result = []
    for r1 in range(h + 1):
        for r2 in range(r1 + 1, h + 1):
            for c1 in range(w + 1):
                sum_r = sum_matrix[r2 - 1, c1 - 1]
                if r1 > 0:
                    sum_r -= sum_matrix[r1 - 1, c1 - 1]
                if sum_r == 382:
                    result.append(matrix[r1:r2, :])
                for c2 in range(c1 + 1, w + 1):
                    sum_r = sum_matrix[r2 - 1, c2 - 1]
                    if r1 > 0:
                        sum_r -= sum_matrix[r1 - 1, c2 - 1]
                    if sum_r == 382:
                        result.append(matrix[r1:r2, c1:c2])
    return result