import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 1):
        for j in range(cols - 1):
            if matrix[i, j] == 45:
                if matrix[i, j + 1] == 45 and matrix[i + 1, j] == 45 and (matrix[i + 1, j + 1] == 45):
                    count += 1
    return count