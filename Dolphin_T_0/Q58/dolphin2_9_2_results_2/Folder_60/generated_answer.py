import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 88
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for x in range(i, rows):
                for y in range(j, cols):
                    if np.count_nonzero(matrix[i:x + 1, j:y + 1]) == n:
                        count += 1
    return count