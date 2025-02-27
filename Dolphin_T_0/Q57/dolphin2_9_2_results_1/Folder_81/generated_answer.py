import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    row_count, col_count = matrix.shape
    for row in range(row_count):
        for col in range(col_count):
            for size in range(2, min(row_count - row + 1, col_count - col + 1) + 1):
                submatrix_sum = np.sum(matrix[row:row + size, col:col + size])
                if submatrix_sum == -90:
                    submatrices.append(matrix[row:row + size, col:col + size])
    return submatrices