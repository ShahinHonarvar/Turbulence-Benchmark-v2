import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 39:
                for row in range(i, rows):
                    for col in range(j, cols):
                        if np.array_equal(matrix[row, col], matrix[i, j]) and (row - i + 1) * (col - j + 1) == 39:
                            count += 1
    return count