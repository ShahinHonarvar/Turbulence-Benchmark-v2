import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 54
    count = 0
    for r in range(0, rows - n + 1):
        for c in range(0, cols - n + 1):
            sub_matrix = matrix[r:r + n, c:c + n]
            if np.count_nonzero(sub_matrix) == n:
                count += 1
    return count