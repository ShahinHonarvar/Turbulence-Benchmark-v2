import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 83
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + n - 1 < rows and j + n - 1 < cols:
                submatrix = matrix[i:i + n, j:j + n]
                if np.count_nonzero(submatrix == 83) == n:
                    count += 1
    return count