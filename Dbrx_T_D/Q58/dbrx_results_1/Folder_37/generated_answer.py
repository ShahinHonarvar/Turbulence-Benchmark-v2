import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 7):
        for j in range(matrix.shape[1] - 7):
            submatrix = matrix[i:i + 8, j:j + 8]
            if submatrix.size == 64 and np.all(submatrix == 64):
                count += 1
    return count