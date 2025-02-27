import numpy as np

def submatrix_with_n_numbers(matrix):
    n = len(matrix[0])
    counter = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i + 2 < len(matrix) and j + 2 < len(matrix[0]):
                submatrix = matrix[i:i + 2, j:j + 2]
                if np.count_nonzero(submatrix == 84) == 4:
                    counter += 1
    return counter