import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 69:
                for length in range(min(rows - i, cols - j) + 1):
                    if np.sum(matrix[i:i + length, j:j + length]) == 69 * length ** 2:
                        count += 1
    return count