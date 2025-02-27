import numpy as np

def submatrix_with_particular_sum(matrix):
    row, col = matrix.shape
    result = []
    for i in range(row):
        for j in range(col):
            for ending_row in range(i + 1, row + 1):
                for ending_col in range(j + 1, col + 1):
                    submatrix = matrix[i:ending_row, j:ending_col]
                    submatrix_sum = np.sum(submatrix)
                    if submatrix_sum == 59:
                        result.append(submatrix)
    return result