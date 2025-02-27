import numpy as np

def submatrix_with_n_numbers(matrix):
    if len(matrix.shape) != 2 or matrix.shape[0] < 95 or matrix.shape[1] < 95:
        return 0
    count = 0
    for i in range(matrix.shape[0] - 95 + 1):
        for j in range(matrix.shape[1] - 95 + 1):
            submatrix = matrix[i:i + 95, j:j + 95]
            if np.all(submatrix == 95):
                count += 1
    return count