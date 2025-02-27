import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    height, width = matrix.shape
    for i in range(0, height - 2):
        for j in range(0, width - 2):
            if np.all(matrix[i:i + 3, j:j + 3] == 144):
                submatrix_count += 1
    return submatrix_count