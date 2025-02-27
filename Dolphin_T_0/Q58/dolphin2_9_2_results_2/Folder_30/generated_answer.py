import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if i + 10 <= n and j + 10 <= m:
                submatrix = matrix[i:i + 10, j:j + 10]
                if np.count_nonzero(submatrix) == 94:
                    count += 1
    return count