import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            if len(np.unique(matrix[i:i + 2, j:j + 2])) == 8:
                count += 1
    return count