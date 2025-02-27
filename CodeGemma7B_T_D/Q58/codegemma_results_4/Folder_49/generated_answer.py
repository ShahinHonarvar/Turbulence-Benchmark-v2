import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    result = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows):
                for l in range(j + 1, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.size == 72 and (submatrix == 27).sum() == 72:
                        result += 1
    return result