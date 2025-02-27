import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            for k in range(i, rows + 1):
                for l in range(j, cols + 1):
                    if np.size(matrix[i - 1:k, j - 1:l]) == 193:
                        count += 1
    return count