import numpy as np

def submatrix_with_n_numbers(a):
    n = a.shape[0]
    count = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    x = a[i][j]
                    y = a[j][k]
                    z = a[k][l]
                    w = a[l][i]
                    t = x + y + z + w
                    if t == 20:
                        count += 1
    return count