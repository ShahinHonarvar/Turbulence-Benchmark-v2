import numpy as np

def submatrix_with_n_numbers(matrix):
    row, col = matrix.shape
    count = 0
    for i in range(row):
        for j in range(col):
            if i + 12 < row and j + 12 < col:
                submatrix = matrix[i:i + 12, j:j + 12]
                if submatrix.size == 144:
                    count += 1
    return count