import numpy as np

def submatrix_with_n_numbers(matrix):
    height, width = matrix.shape
    length = 4
    count = 0
    for y in range(0, height - length + 1):
        for x in range(0, width - length + 1):
            if np.sum(matrix[y:y + length, x:x + length]) == 16:
                count += 1
    return count