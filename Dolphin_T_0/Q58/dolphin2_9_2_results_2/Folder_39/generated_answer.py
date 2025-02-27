import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                if verify_submatrix(matrix, i, j, 59):
                    count += 1
    return count

def verify_submatrix(matrix, row, col, n):
    try:
        if row + n > matrix.shape[0] or col + n > matrix.shape[1]:
            return False
        submatrix = matrix[row:row + n, col:col + n]
        return np.all(submatrix == 1)
    except:
        return False