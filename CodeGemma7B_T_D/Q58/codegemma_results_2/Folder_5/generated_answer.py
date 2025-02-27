import numpy as np

def submatrix_with_n_numbers(matrix):
    ans = 0
    for r1 in range(len(matrix)):
        for c1 in range(len(matrix[0])):
            for r2 in range(r1, len(matrix)):
                for c2 in range(c1, len(matrix[0])):
                    a = matrix[r1:r2 + 1]
                    tmp = 0
                    for i in range(len(a)):
                        tmp += 2 ** i * a[i][c1:c2 + 1].sum()
                    if tmp == 63:
                        ans += 1
    return ans