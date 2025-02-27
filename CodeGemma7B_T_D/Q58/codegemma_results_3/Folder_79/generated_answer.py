import numpy as np

def submatrix_with_n_numbers(matrix):
    """Returns the number of submatrices with n numbers"""
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            for r in range(row, len(matrix)):
                for c in range(col, len(matrix[0])):
                    if np.sum(matrix[row:r + 1, col:c + 1]) == 60:
                        count += 1
    return count