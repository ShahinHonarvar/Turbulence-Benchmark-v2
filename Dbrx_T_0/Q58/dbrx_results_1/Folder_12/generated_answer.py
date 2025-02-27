import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 4):
        for j in range(matrix.shape[1] - 6):
            submatrix = matrix[i:i + 5, j:j + 7]
            if np.isin(submatrix, 46).sum() == 46:
                count += 1
    return count