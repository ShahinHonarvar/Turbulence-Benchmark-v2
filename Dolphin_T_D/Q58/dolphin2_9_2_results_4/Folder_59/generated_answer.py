import numpy as np

def submatrix_with_n_numbers(matrix):
    n = len(matrix[0])
    m = len(matrix)
    count = 0
    for i in range(m):
        for j in range(n):
            if i + 13 < m and j + 8 < n:
                submatrix = []
                for k in range(13):
                    for l in range(8):
                        submatrix.append(matrix[i + k][j + l])
                submatrix = list(set(submatrix))
                if len(submatrix) == 76:
                    count += 1
    return count