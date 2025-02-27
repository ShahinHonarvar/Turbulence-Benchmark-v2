import numpy as np

def submatrix_with_n_numbers(matrix):
    if len(matrix) < 14 or len(matrix[0]) < 14:
        return 0
    count = 0
    for i in range(len(matrix) - 13):
        for j in range(len(matrix[0]) - 13):
            submatrix = matrix[i:i + 14, j:j + 14]
            if np.sum(submatrix) == 193:
                count += 1
    return count