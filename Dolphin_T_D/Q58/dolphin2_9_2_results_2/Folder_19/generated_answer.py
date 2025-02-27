import numpy as np

def submatrix_with_n_numbers(matrix):
    matrix_rows, matrix_columns = matrix.shape
    count = 0
    for i in range(matrix_rows):
        for j in range(matrix_columns):
            if i + 3 < matrix_rows and j + 3 < matrix_columns:
                submatrix = np.array([[matrix[i][j], matrix[i][j + 1], matrix[i][j + 2], matrix[i][j + 3]], [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2], matrix[i + 1][j + 3]], [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2], matrix[i + 2][j + 3]], [matrix[i + 3][j], matrix[i + 3][j + 1], matrix[i + 3][j + 2], matrix[i + 3][j + 3]]])
                if np.count_nonzero(submatrix == 17) == 16:
                    count += 1
    return count