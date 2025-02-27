import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if i + 3 < matrix.shape[0] and j + 3 < matrix.shape[1]:
                submatrix = matrix[i:i + 4, j:j + 4]
                if np.count_nonzero(submatrix == 84) == 16:
                    count += 1
    return count