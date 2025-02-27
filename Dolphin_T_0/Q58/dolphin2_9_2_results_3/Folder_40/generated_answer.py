import numpy as np

def submatrix_with_n_numbers(matrix):
    n = matrix.shape[0]
    if n == 1:
        return 0
    count = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                if i + 1 < n:
                    count += 1
                if j + 1 < n:
                    count += 1
    return count