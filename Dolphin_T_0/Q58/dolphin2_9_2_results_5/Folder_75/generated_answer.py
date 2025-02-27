import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 9):
        for j in range(matrix.shape[1] - 9):
            if np.sum(matrix[i:i + 10, j:j + 10] == 80) == 80:
                count += 1
    return count