import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    count = 0
    for i in range(rows - 1):
        for j in range(cols - 1):
            if matrix[i][j] == 47:
                if matrix[i + 1][j] == 47 and matrix[i][j + 1] == 47 and (matrix[i + 1][j + 1] == 47):
                    count += 1
    return count