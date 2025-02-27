import numpy as np

def submatrix_with_n_numbers(matrix):
    n_numbers = 78
    count = 0
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            for x in range(i, m):
                for y in range(j, n):
                    if np.sum(matrix[i:x + 1, j:y + 1]) == n_numbers:
                        count += 1
    return count if count else 0