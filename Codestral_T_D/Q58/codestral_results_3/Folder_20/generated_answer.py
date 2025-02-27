import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 49
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 6):
        for j in range(cols - 6):
            for k in range(i + 7, rows + 1):
                for l in range(j + 7, cols + 1):
                    if np.sum(matrix[i:k, j:l] == 49) == n:
                        count += 1
    return count