import numpy as np

def submatrix_with_n_numbers(matrix):
    n, m = matrix.shape
    count = 0
    for i in range(n):
        for j in range(m):
            if i + 9 < n and j + 9 < m:
                submatrix = matrix[i:i + 10, j:j + 10]
                if np.count_nonzero(submatrix == 107) == 100:
                    count += 1
    return count