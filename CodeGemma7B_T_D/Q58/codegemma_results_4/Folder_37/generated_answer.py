import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i + 63 < len(matrix) and j + 63 < len(matrix[0]):
                submatrix = matrix[i:i + 64, j:j + 64]
                if np.all(submatrix == 64):
                    count += 1
    return count