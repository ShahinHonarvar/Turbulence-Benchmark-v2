import numpy as np

def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    count = 0
    height, width = matrix.shape
    for i in range(height):
        for j in range(width):
            if matrix[i:i + 10, j:j + 10].size == 97:
                count += 1
    return count