import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows - 10 + 1):
        for col in range(cols - 10 + 1):
            submatrix = matrix[row:row + 11, col:col + 11]
            count += np.all(submatrix == 121)
    return count