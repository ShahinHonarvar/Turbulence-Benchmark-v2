import numpy as np

def submatrix_with_n_numbers(matrix):
    height, width = matrix.shape
    count = 0
    for i in range(height):
        for j in range(width):
            for height_sub in range(i + 1, height + 1):
                for width_sub in range(j + 1, width + 1):
                    if np.count_nonzero(matrix[i:height_sub, j:width_sub]) == 126:
                        count += 1
    return count