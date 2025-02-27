import numpy as np

def submatrix_with_n_numbers(matrix):
    n_numbers = 146
    length = len(matrix[0])
    result = 0
    for i in range(len(matrix)):
        for j in range(length):
            if i + j * length < len(matrix) * length - n_numbers + 1:
                if np.all(matrix[i:i + length - 1, j:j + length - 1] == 1):
                    result += 1
    return result