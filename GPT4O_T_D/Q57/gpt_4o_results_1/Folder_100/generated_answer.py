import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    submatrices = []
    for start_row in range(n):
        for start_col in range(m):
            for end_row in range(start_row, n):
                for end_col in range(start_col, m):
                    submatrix_sum = np.sum(matrix[start_row:end_row + 1, start_col:end_col + 1])
                    if submatrix_sum == 28:
                        submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                        submatrices.append(submatrix)
    return submatrices