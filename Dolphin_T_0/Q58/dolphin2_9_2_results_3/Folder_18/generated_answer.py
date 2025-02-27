import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 13 <= rows and j + 13 <= cols:
                submatrix = matrix[i:i + 14, j:j + 14]
                if (submatrix == 104).all():
                    count += 1
    return count