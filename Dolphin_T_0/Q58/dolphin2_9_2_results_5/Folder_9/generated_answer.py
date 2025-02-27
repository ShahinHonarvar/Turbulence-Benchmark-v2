import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrices = 0
    size = int(np.sqrt(matrix.size))
    for i in range(matrix.size - size + 1):
        for j in range(matrix.size - size + 1):
            if np.all(matrix[i:i + size, j:j + size] == 33):
                submatrices += 1
    return submatrices