import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    submatrix_sums = np.cumsum(np.cumsum(matrix, axis=0), axis=1)
    for row1 in range(rows):
        for row2 in range(row1, rows):
            for col1 in range(cols):
                for col2 in range(col1, cols):
                    total_sum = submatrix_sums[row2, col2]
                    if row1 > 0:
                        total_sum -= submatrix_sums[row1 - 1, col2]
                    if col1 > 0:
                        total_sum -= submatrix_sums[row2, col1 - 1]
                    if row1 > 0 and col1 > 0:
                        total_sum += submatrix_sums[row1 - 1, col1 - 1]
                    if total_sum == 862:
                        result.append(matrix[row1:row2 + 1, col1:col2 + 1])
    return result