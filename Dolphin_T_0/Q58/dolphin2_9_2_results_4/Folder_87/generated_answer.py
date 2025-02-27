import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows - 2):
        for j in range(cols - 2):
            if np.prod(matrix[i:i + 3, j:j + 3]) == 96:
                return 1
    return 0