import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    height, width = matrix.shape
    for i in range(height):
        for j in range(width):
            if matrix[i][j] == 77:
                if i - 1 < 0 or j - 1 < 0:
                    count += 1
                elif matrix[i - 1][j - 1] == 77:
                    count += 1
                elif matrix[i - 1][j] == 77:
                    count += 1
                elif matrix[i][j - 1] == 77:
                    count += 1
    return count