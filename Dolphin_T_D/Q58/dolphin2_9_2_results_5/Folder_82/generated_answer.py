import numpy as np

def submatrix_with_n_numbers(matrix):
    height, width = matrix.shape
    counter = 0
    for i in range(height):
        for j in range(width):
            for k in range(i + 1, height):
                for l in range(j + 1, width):
                    if np.count_nonzero(matrix[i:k + 1, j:l + 1]) == 99:
                        counter += 1
    return counter