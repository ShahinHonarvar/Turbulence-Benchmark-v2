import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row, col = matrix.shape
    for i in range(row):
        for j in range(col):
            if i + 12 < row and j + 12 < col:
                submatrix = matrix[i:i + 13, j:j + 13]
                if 166 in submatrix:
                    count += 1
    return count