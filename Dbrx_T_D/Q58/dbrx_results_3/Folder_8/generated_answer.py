import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    n = 29
    matrix_rows = np.shape(matrix)[0]
    matrix_cols = np.shape(matrix)[1]
    for row in range(matrix_rows - n + 1):
        for col in range(matrix_cols - n + 1):
            submatrix = matrix[row:row + n, col:col + n]
            if np.size(submatrix) == n * n:
                submatrix_count += 1
                print('Submatrix at row ', row + 1, 'and column ', col + 1, 'with elements: \n', submatrix, '\n')
    return submatrix_count