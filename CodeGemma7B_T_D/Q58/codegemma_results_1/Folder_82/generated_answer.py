import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(i + 1, rows):
            for k in range(cols):
                for l in range(k + 1, cols):
                    submatrix = matrix[i:j + 1, k:l + 1]
                    if (submatrix == 99).all():
                        count += 1
    return count