import numpy as np

def submatrix_with_n_numbers(matrix, n=2):
    count = 0
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 2:
                if i + 2 <= m and j + 2 <= n:
                    if np.all(matrix[i:i + 2, j:j + 2] == 2):
                        count += 1
    return count