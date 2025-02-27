import numpy as np

def submatrix_with_n_numbers(matrix):
    size = matrix.shape
    count = 0
    for i in range(size[0]):
        for j in range(size[1]):
            if matrix[i, j] == 66:
                for x in range(i + 1, size[0]):
                    if (x - i) * (size[1] - j) == 65:
                        count += 1
    return count