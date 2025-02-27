import numpy as np

def submatrix_with_n_numbers(matrix, n=16):
    size = np.shape(matrix)
    count = 0
    for i in range(size[0] - 3):
        for j in range(size[1] - 3):
            submatrix = matrix[i:i + 4, j:j + 4]
            if submatrix.size == n:
                count += 1
    return count