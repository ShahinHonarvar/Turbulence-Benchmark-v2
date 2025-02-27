import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row, rows):
                for end_col in range(start_col, cols):
                    submatrix_sum = np.sum(matrix[start_row:end_row + 1, start_col:end_col + 1])
                    if submatrix_sum == 411:
                        submatrices.append(matrix[start_row:end_row + 1, start_col:end_col + 1].tolist())
    return submatrices