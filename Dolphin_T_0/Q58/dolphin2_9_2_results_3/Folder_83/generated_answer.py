import numpy as np

def submatrix_with_n_numbers(matrix):
    height, width = matrix.shape
    count = 0
    for i in range(height):
        for j in range(width):
            for k in range(i, height):
                for l in range(j, width):
                    if (k - i + 1) * (l - j + 1) == 47:
                        count += 1
    return count