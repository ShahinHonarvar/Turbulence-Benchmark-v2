import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    height, width = matrix.shape
    for i in range(height - 2):
        for j in range(width - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.count_nonzero(submatrix == 83) == 83:
                count += 1
    return count