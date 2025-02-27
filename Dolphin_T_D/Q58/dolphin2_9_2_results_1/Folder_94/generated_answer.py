import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 93:
                n_size = 1
                for k in range(1, min(rows - i, cols - j)):
                    if matrix[i + k, j + k] == 93:
                        n_size += 1
                    else:
                        break
                count += n_size
    return count