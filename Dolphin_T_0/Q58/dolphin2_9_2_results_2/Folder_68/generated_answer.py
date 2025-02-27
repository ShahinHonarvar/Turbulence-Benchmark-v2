import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, columns = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(columns):
            if isinstance(matrix[i][j], int):
                if len(matrix[i][j:j + 74].shape) == 1:
                    count += 1
                if len(matrix[i:i + 74, j].shape) == 1:
                    count += 1
    return count