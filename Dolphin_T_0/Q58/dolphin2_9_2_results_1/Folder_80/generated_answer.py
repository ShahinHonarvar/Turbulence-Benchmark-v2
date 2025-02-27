import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for m in range(rows - i):
                for n in range(cols - j):
                    if np.sum(matrix[i:i + m + 1, j:j + n + 1]) == 180:
                        count += 1
    return count