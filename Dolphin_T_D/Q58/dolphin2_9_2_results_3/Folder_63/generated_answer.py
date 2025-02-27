import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 57:
                count += 1
                for k in range(i + 1, rows):
                    for l in range(j + 1, cols):
                        if matrix[k][l] == 57:
                            count += 1
    return count if count else 0