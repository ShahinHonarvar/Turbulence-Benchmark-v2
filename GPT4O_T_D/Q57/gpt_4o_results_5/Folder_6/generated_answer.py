import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(mat, r1, c1, r2, c2):
        return np.sum(mat[r1:r2, c1:c2])
    result = []
    rows, cols = matrix.shape
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row + 1, rows + 1):
                for end_col in range(start_col + 1, cols + 1):
                    if submatrix_sum(matrix, start_row, start_col, end_row, end_col) == 126:
                        result.append(matrix[start_row:end_row, start_col:end_col].tolist())
    return result