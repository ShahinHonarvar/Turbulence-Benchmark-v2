import numpy as np

def submatrix_with_n_numbers(matrix):
    n = matrix.shape[0]
    count = 0
    for i in range(n):
        for j in range(n):
            if i + 17 <= n and j + 20 <= n:
                submatrix = matrix[i:i + 17, j:j + 20]
                if np.count_nonzero(submatrix == 1) == 130:
                    count += 1
    return count