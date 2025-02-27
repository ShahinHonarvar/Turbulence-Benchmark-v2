import numpy as np

def submatrix_with_n_numbers(matrix):
    n_elements = 99
    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i + n_elements <= len(matrix) and j + n_elements <= len(matrix[i]):
                submatrix = matrix[i:i + n_elements, j:j + n_elements]
                if np.count_nonzero(submatrix) == n_elements:
                    result += 1
    return result