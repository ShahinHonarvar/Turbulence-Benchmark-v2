import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for size in range(1, matrix.shape[0] + 1):
        for i in range(matrix.shape[0] - size + 1):
            for j in range(matrix.shape[1] - size + 1):
                if np.sum(matrix[i:i + size, j:j + size]) == 28:
                    count += 1
    return count