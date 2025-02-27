import numpy as np

def submatrix_with_n_numbers(matrix):
    size = matrix.shape
    count = 0
    for i in range(size[0] - 3):
        for j in range(size[1] - 3):
            if i + 4 <= size[0] and j + 4 <= size[1] and (np.sum(matrix[i:i + 4, j:j + 4]) == 64):
                count += 1
    return count