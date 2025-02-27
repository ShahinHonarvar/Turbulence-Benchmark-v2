import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 97
    result = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if x + n <= len(matrix) and y + n <= len(matrix[0]):
                if np.all(matrix[x:x + n, y:y + n] == n):
                    result += 1
    return result