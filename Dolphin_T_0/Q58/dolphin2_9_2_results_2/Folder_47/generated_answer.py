import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    total = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows):
                for l in range(j + 1, cols):
                    if len(matrix[i:k + 1, j:l + 1].reshape(-1)) == 90:
                        total += 1
    if total == 0:
        return 0
    else:
        return total