import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    matrix = np.array(matrix)
    height, width = matrix.shape
    for i in range(height):
        for j in range(width):
            for k in range(i + 2, height + 1):
                for l in range(j + 2, width + 1):
                    if np.sum(matrix[i:k, j:l]) == 2:
                        count += 1
    return count