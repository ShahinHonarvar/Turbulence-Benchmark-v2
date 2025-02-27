import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = (len(matrix), len(matrix[0]))
    pit = [[0] * m for _ in range(n)]
    for k in range(n):
        for l in range(m):
            pit[k][l] = matrix[k][l] if k == 0 or l == 0 else pit[0][l] + matrix[k][l] + pit[k][0]
    res = []
    for k in range(n):
        for l in range(m):
            for i in range(k, n):
                for j in range(l, m):
                    if pit[i][j] - pit[k - 1][j] - pit[i][l - 1] + pit[k - 1][l - 1] == 87:
                        res.append(matrix[k:i + 1, l:j + 1])
    return res