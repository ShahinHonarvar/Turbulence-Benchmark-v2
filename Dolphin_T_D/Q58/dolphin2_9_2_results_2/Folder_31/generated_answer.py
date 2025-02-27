import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 45
    dimensions = matrix.shape
    count = 0
    for i in range(dimensions[0] - n + 1):
        for j in range(dimensions[1] - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.count_nonzero(submatrix == 0) == n * n:
                count += 1
    return count