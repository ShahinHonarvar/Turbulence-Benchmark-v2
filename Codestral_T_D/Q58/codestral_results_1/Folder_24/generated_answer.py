import numpy as np

def submatrix_with_n_numbers(matrix, n=51):
    row, col = matrix.shape
    count = 0
    for i in range(row):
        for j in range(col):
            for k in range(i, row):
                for l in range(j, col):
                    if np.sum(matrix[i:k + 1, j:l + 1]) == n:
                        count += 1
    return count