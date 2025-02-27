import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    counter = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 37:
                if i > 0 and j > 0:
                    if matrix[i - 1][j - 1] == 37 and matrix[i - 1][j] == 37 and (matrix[i][j - 1] == 37):
                        counter += 1
                if i > 0:
                    if matrix[i - 1][j] == 37:
                        counter += 1
                if j > 0:
                    if matrix[i][j - 1] == 37:
                        counter += 1
    return counter