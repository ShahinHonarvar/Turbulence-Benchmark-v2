import numpy as np

def submatrix_with_n_numbers(matrix):
    result = 0
    for i in range(len(matrix) - 2):
        for j in range(len(matrix[0]) - 2):
            if len(np.unique(matrix[i:i + 3, j:j + 3])) == 23:
                result += 1
    return result