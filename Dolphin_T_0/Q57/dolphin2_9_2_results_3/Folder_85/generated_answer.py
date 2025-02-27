import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for row in range(rows):
        for col in range(cols):
            for r in range(row, rows):
                for c in range(col, cols):
                    submatrix_sum = np.sum(matrix[row:r + 1, col:c + 1])
                    if submatrix_sum == -87:
                        result.append(matrix[row:r + 1, col:c + 1])
    return result