import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i, j in np.ndindex(matrix.shape):
        for a in range(i + 1, matrix.shape[0] + 1):
            for b in range(j + 1, matrix.shape[1] + 1):
                submatrix = matrix[i:a, j:b]
                if np.all(submatrix == 115):
                    count += 1
    return count