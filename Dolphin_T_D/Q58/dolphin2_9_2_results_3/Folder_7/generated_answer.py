import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for row in range(i + 1, rows):
                for col in range(j + 1, cols):
                    if np.count_nonzero(matrix[i:row, j:col]) == 121:
                        count += 1
    return count