import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    size = matrix.shape[0]
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 43:
                for k in range(i + 1, size + 1):
                    for l in range(j + 1, size + 1):
                        if np.count_nonzero(matrix[i:k, j:l]) == 43:
                            count += 1
    return count