import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 4
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == n:
                try:
                    if matrix[i + 1, j] == n and matrix[i, j + 1] == n and (matrix[i + 1, j + 1] == n):
                        count += 1
                except:
                    continue
    return count