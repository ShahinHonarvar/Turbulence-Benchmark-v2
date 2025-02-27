import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i:i + 11, j:j + 11].shape[0] == 11 and matrix[i:i + 11, j:j + 11].shape[1] == 11 and (np.sum(matrix[i:i + 11, j:j + 11]) == 93):
                count += 1
    return count