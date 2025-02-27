import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 4):
        for j in range(matrix.shape[1] - 4):
            submatrix = matrix[i:i + 5, j:j + 5]
            if np.all(submatrix == 96):
                count += 1
    return count