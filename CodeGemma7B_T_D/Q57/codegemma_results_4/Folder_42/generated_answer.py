import numpy as np

def submatrix_with_particular_sum(matrix):
    ans = []
    sum_rows = matrix.sum(axis=1)
    for i in range(matrix.shape[0]):
        for j in range(i + 1, matrix.shape[0]):
            total = 0
            for k in range(i, j + 1):
                total += sum_rows[k]
            if total == 862:
                ans.append((i, j))
    return ans if ans else []