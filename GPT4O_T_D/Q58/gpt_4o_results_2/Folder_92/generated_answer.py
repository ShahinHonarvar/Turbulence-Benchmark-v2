import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    if rows < 2 or cols < 4:
        return 0
    count = 0
    for i in range(rows - 1):
        for j in range(cols - 3):
            if matrix[i][j:j + 4].size + matrix[i + 1][j:j + 4].size == 8:
                count += 1
    return count