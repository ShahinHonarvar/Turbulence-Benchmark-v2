import numpy as np

def submatrix_with_n_numbers(matrix):
    row = matrix.shape[0]
    col = matrix.shape[1]
    count = 0
    for i in range(row):
        for j in range(col):
            for k in range(1, min(row, col) + 1):
                if i + k - 1 < row and j + k - 1 < col:
                    if np.sum(matrix[i:i + k, j:j + k]) == 15:
                        count += 1
    return count