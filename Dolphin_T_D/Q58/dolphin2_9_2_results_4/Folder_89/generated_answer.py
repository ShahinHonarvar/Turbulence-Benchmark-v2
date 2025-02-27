import numpy as np

def submatrix_with_n_numbers(matrix):
    row, col = matrix.shape
    count = 0
    for i in range(row - 3):
        for j in range(col - 3):
            if mat[i:i + 4, j:j + 4].size == 18:
                count += 1
    if count == 0:
        return 0
    return count