import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i + 1, matrix.shape[0]):
                for l in range(j + 1, matrix.shape[1]):
                    temp_matrix = matrix[i:k + 1, j:l + 1]
                    if np.count_nonzero(temp_matrix == 88) == 88:
                        count += 1
    return count