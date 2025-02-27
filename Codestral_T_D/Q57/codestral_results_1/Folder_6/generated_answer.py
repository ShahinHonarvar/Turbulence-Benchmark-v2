import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for size in range(1, rows * cols + 1):
        for i in range(rows):
            for j in range(cols):
                submatrix_rows = min(size, rows - i)
                submatrix_cols = min(size, cols - j)
                submatrix = matrix[i:i + submatrix_rows, j:j + submatrix_cols]
                if np.sum(submatrix) == 126:
                    submatrices.append(submatrix)
    return submatrices