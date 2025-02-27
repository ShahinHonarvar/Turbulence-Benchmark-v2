import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 118:
                for k in range(i, rows):
                    for l in range(j, cols):
                        if len(matrix[k:k + i + 1, l:l + j + 1]) == 118:
                            count += 1
    return count if count else 0