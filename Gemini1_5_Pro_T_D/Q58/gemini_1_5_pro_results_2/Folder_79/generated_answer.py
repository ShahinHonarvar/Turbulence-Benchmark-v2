import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = (len(matrix), len(matrix[0]))
    count = 0
    for i in range(m - 5):
        for j in range(n - 5):
            for k in range(i + 6, m + 1):
                for l in range(j + 6, n + 1):
                    submatrix = matrix[i:k, j:l]
                    if submatrix.size == 60:
                        count += 1
    return count