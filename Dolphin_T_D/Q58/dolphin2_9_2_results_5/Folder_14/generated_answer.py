import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.size % 84 != 0:
        return 0
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if i + 3 < matrix.shape[0] and j + 4 < matrix.shape[1]:
                if len(np.where(matrix[i:i + 4, j:j + 4] == 84)[0]) == 84:
                    count += 1
    return count