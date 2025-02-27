import numpy as np

def submatrix_with_n_numbers(matrix):
    height, width = matrix.shape
    count = 0
    for i in range(height):
        for j in range(width):
            for k in range(i + 1, height):
                for l in range(j + 1, width):
                    if np.sum(matrix[i:k, j:l]) == 193:
                        count += 1
    return count