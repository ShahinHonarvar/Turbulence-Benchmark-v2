import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 2):
        for j in range(len(matrix[0]) - 2):
            if np.all(matrix[i:i + 3, j:j + 3] == 1):
                count += 1
    return count