import numpy as np

def submatrix_with_n_numbers(matrix, n=87):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    if matrix[i:k + 1, j:l + 1].size == n and np.sum(matrix[i:k + 1, j:l + 1]) == 87 * n:
                        count += 1
    return count