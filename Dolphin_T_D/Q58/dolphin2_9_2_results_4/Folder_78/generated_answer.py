import numpy as np

def submatrix_with_n_numbers(matrix):
    total = 0
    for i in range(matrix.shape[0] - 8):
        for j in range(matrix.shape[1] - 8):
            submatrix = matrix[i:i + 9, j:j + 9]
            if np.sum(submatrix == 91) == 9:
                total += 1
    return total