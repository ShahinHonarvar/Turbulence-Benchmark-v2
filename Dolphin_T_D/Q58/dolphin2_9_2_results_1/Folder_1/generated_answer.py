import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    count = 0
    for i in range(rows - 2):
        for j in range(cols - 2):
            submatrix_sum = np.sum(matrix[i:i + 3, j:j + 3])
            if submatrix_sum == 23:
                count += 1
    return count