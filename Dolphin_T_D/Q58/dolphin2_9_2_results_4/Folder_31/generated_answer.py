import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    shape = matrix.shape
    for i in range(shape[0]):
        for j in range(shape[1]):
            if i + 3 < shape[0] and j + 3 < shape[1]:
                if np.sum(matrix[i:i + 4, j:j + 4]) == 45:
                    count += 1
    return count