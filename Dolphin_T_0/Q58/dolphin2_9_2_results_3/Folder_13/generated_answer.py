import numpy as np

def submatrix_with_n_numbers(matrix):
    _, rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for r in range(i, rows):
                for c in range(j, cols):
                    if matrix[i:r + 1, j:c + 1].size == 175:
                        count += 1
    return count