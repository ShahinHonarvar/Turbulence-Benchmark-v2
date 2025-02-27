import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m - 146):
        for j in range(n - 146):
            for k in range(i + 147, m + 1):
                for l in range(j + 147, n + 1):
                    submatrix = matrix[i:k, j:l]
                    if submatrix.size == 147:
                        count += 1
    return count