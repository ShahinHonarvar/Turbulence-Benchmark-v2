import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submates = 0
    for i in range(rows - 2):
        for j in range(cols - 2):
            submat = matrix[i:i + 3, j:j + 3]
            if np.sum(submat) == 45:
                submates += 1
    return submates