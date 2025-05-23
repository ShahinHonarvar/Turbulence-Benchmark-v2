import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for i in range(rows - 3):
        for j in range(columns - 3):
            submatrix = matrix[i:i + 4, j:j + 4]
            if np.sum(submatrix) == 28:
                count += 1
    return count