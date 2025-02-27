import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for m in range(i + 1, matrix.shape[0]):
                for n in range(j + 1, matrix.shape[1]):
                    if np.all(matrix[i:m + 1, j:n + 1] == 1):
                        count += 1
    return count