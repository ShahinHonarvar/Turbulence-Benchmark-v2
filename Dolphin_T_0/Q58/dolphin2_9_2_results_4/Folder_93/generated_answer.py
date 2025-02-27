import numpy as np

def submatrix_with_n_numbers(matrix):
    row, col = matrix.shape
    count = 0
    for i in range(row):
        for j in range(col):
            for k in range(i + 1, row + 1):
                for l in range(j + 1, col + 1):
                    submatrix = matrix[i:k, j:l]
                    if len(submatrix) == 53:
                        count += 1
    return count if count > 0 else 0