import numpy as np

def submatrix_with_n_numbers(matrix):
    row, col = matrix.shape
    counter = 0
    for i in range(row):
        for j in range(col):
            if i + 2 < row and j + 3 < col:
                submatrix = matrix[i:i + 2, j:j + 3]
                if np.count_nonzero(submatrix == 120) == 4:
                    counter += 1
    return counter