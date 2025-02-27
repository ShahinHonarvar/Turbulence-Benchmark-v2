import numpy as np

def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    submatrices = np0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i + 3 < len(matrix) and j + 3 < len(matrix[0]):
                submatrix = matrix[i:i + 3, j:j + 3]
                if np.count_nonzero(submatrix) == 97:
                    submatrices += 1
    return submatrices