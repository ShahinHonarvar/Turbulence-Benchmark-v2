import numpy as np

def submatrix_with_n_numbers(matrix):
    n = len(matrix)
    m = len(matrix[0])
    count = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 5:
                if i + 1 < n and j + 1 < m:
                    if matrix[i + 1][j] == 5 and matrix[i][j + 1] == 5 and (matrix[i + 1][j] == 5):
                        count += 1
    return count