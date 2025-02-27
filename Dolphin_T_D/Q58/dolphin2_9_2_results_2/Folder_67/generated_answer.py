import numpy as np

def submatrix_with_n_numbers(matrix):
    row, col = matrix.shape
    count = 0
    for i in range(row):
        for j in range(col):
            for k in range(i + 1, row + 1):
                for l in range(j + 1, col + 1):
                    if np.count_nonzero(matrix[i:k, j:l]) == 43:
                        count += 1
    return count