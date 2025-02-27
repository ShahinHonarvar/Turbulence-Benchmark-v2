import numpy as np

def submatrix_with_n_numbers(matrix):
    row, col = matrix.shape
    count = 0
    for i in range(row - 6):
        for j in range(col - 6):
            if matrix[i][j] + matrix[i + 1][j] + matrix[i + 2][j] + matrix[i + 3][j] + matrix[i][j + 1] + matrix[i + 1][j + 1] + matrix[i + 2][j + 1] + matrix[i + 3][j + 1] + matrix[i][j + 2] + matrix[i + 1][j + 2] + matrix[i + 2][j + 2] + matrix[i + 3][j + 2] + matrix[i][j + 3] + matrix[i + 1][j + 3] + matrix[i + 2][j + 3] + matrix[i + 3][j + 3] + matrix[i][j + 4] + matrix[i + 1][j + 4] + matrix[i + 2][j + 4] + matrix[i + 3][j + 4] + matrix[i][j + 5] + matrix[i + 1][j + 5] + matrix[i + 2][j + 5] + matrix[i + 3][j + 5] + matrix[i][j + 6] + matrix[i + 1][j + 6] + matrix[i + 2][j + 6] + matrix[i + 3][j + 6] + matrix[i + 4][j] + matrix[i + 5][j] + matrix[i + 6][j] + matrix[i + 7][j] + matrix[i + 4][j + 1] + matrix[i + 5][j + 1] + matrix[i + 6][j + 1] + matrix[i + 7][j + 1] + matrix[i + 4][j + 2] + matrix[i + 5][j + 2] + matrix[i + 6][j + 2] + matrix[i + 7][j + 2] + matrix[i + 4][j + 3] + matrix[i + 5][j + 3] + matrix[i + 6][j + 3] + matrix[i + 7][j + 3] + matrix[i + 4][j + 4] + matrix[i + 5][j + 4] + matrix[i + 6][j + 4] + matrix[i + 7][j + 4] + matrix[i + 4][j + 5] + matrix[i + 5][j + 5] + matrix[i + 6][j + 5] + matrix[i + 7][j + 5] + matrix[i + 4][j + 6] + matrix[i + 5][j + 6] + matrix[i + 6][j + 6] + matrix[i + 7][j + 6] == 48:
                count += 1
    return count