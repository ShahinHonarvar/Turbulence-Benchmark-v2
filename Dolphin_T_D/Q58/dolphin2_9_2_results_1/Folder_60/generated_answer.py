import numpy as np

def submatrix_with_n_numbers(matrix):
    n = len(matrix)
    m = len(matrix[0])
    count = 0
    for i in range(n):
        for j in range(m):
            for x in range(1, min(88, n - i)):
                for y in range(1, min(88, m - j)):
                    if sum((sum((matrix[i + a][j + b] for b in range(y))) for a in range(x))) == 88:
                        count += 1
    return count