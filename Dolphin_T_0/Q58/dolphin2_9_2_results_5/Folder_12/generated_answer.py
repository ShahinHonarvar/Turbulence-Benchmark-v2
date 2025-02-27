import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 46:
                if i + 6 < rows and j + 6 < cols:
                    submatrix = matrix[i:i + 6, j:j + 6]
                    count += (submatrix == 46.0).sum().sum()
    return int(count)