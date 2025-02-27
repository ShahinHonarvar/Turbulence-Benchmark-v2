import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for row in range(i, rows):
                for col in range(j, cols):
                    if np.sum(matrix[i:row, j:col]) == 175:
                        count += 1
    return count