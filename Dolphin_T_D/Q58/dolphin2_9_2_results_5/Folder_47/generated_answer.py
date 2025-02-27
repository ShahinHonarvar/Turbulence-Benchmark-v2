import numpy as np

def submatrix_with_n_numbers(matrix):
    n = len(matrix)
    m = len(matrix[0])
    count = 0
    for i in range(n):
        for j in range(m):
            if i + 2 < n and j + 2 < m:
                submatrix_size = matrix[i:i + 3, j:j + 3].size
                if submatrix_size == 9:
                    count += 1
    return count