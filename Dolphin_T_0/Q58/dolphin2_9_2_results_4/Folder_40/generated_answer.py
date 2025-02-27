import numpy as np

def submatrix_with_n_numbers(matrix):
    n = matrix.shape[0]
    count = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                for size in range(2, min(n - i + 1, n - j + 1) + 1):
                    if np.all(matrix[i:i + size, j:j + size] == 1):
                        count += 1
    return count