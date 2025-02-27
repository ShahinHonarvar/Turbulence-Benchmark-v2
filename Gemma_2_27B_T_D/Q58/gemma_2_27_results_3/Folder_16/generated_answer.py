import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    if np.size(matrix[i:k + 1, j:l + 1]) == 154:
                        count += 1
    return count