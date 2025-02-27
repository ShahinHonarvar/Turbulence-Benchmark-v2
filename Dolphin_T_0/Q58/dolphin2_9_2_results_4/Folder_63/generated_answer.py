import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, columns = matrix.shape
    count = 0
    for i in range(rows - 3):
        for j in range(columns - 3):
            if np.sum(matrix[i:i + 4, j:j + 4]) == 57:
                count += 1
    return count