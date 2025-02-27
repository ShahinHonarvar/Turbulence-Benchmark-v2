import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    target = 60
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            if i + target <= m and j + target <= n:
                submatrix = matrix[i:i + target, j:j + target]
                if submatrix.size == target:
                    count += 1
    return count