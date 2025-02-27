import numpy as np

def submatrix_with_n_numbers(matrix):
    m = matrix.shape[0]
    n = matrix.shape[1]
    count = 0
    for i in range(m):
        for j in range(n):
            for k in range(i + 1, m):
                for l in range(j + 1, n):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.size == 104:
                        count += 1
    return count