import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.size == 0 or len(matrix) < 3 or len(matrix[0]) < 3:
        return 0
    row, col = matrix.shape
    count = 0
    for i in range(row - 2):
        for j in range(col - 2):
            if np.sum(matrix[i:i + 3, j:j + 3]) == 111:
                count += 1
    return count