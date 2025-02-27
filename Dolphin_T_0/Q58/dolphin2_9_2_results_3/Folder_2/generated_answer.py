import numpy as np

def submatrix_with_n_numbers(matrix):
    counts = 0
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            if matrix[i, j] == 107:
                count = 1
                for k in range(i + 1, m):
                    for l in range(j + 1, n):
                        if matrix[k, l] == 107:
                            count += 1
                        else:
                            break
                    if count == 107:
                        counts += 1
    return counts