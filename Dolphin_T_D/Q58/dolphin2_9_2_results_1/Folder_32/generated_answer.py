import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if len(matrix) - i >= 10 and len(matrix[0]) - j >= 10:
                count += np.count_nonzero(matrix[i:i + 10, j:j + 10] == 103)
    return count