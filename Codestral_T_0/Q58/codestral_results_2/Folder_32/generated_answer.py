import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 103
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i + n - 1, rows):
                for l in range(j + n - 1, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.size == n:
                        count += 1
    return count