import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for size in range(1, min(matrix.shape[0], matrix.shape[1]) + 1):
        if size * size == 35:
            for i in range(matrix.shape[0] - size + 1):
                for j in range(matrix.shape[1] - size + 1):
                    submatrix = matrix[i:i + size, j:j + size]
                    count += 1
    return count