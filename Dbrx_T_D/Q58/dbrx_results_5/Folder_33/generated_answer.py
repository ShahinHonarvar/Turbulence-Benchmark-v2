import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            target = np.full((3, 3), 118)
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.array_equal(submatrix, target):
                count += 1
    return count