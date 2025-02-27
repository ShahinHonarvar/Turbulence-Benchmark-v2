import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    height, width = matrix.shape
    for i in range(height):
        for j in range(width):
            for height_sub in range(i, height):
                for width_sub in range(j, width):
                    if np.sum(matrix[i:height_sub + 1, j:width_sub + 1]) == 90:
                        count += 1
    return count