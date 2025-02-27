import numpy as np

def submatrix_with_n_numbers(matrix):
    height, width = matrix.shape
    count = 0
    for i in range(height):
        for j in range(width):
            for k in range(i + 1, height + 1):
                for l in range(j + 1, width + 1):
                    if np.sum(matrix[i:k, j:l]) == 121:
                        count += 1
    return count