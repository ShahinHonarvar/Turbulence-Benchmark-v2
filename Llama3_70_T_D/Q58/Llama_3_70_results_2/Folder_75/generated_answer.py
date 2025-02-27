import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for end_col in range(j, n):
                    submatrix = matrix[i:k + 1, j:end_col + 1]
                    if submatrix.size == 80:
                        count += 1
    return count