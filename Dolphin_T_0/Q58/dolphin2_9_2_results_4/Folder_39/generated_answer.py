import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, columns = matrix.shape
    count = 0
    for i in range(rows - 1):
        for j in range(columns - 1):
            for k in range(min(rows - i, columns - j)):
                if np.prod(matrix[i:i + k + 1, j:j + k + 1].shape) == 59:
                    count += 1
    return count