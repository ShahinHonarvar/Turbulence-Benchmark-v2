import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 130:
                if (rows - i) * (cols - j) >= 130:
                    count += 1
    return count