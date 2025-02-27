import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            for r in range(row, len(matrix)):
                for c in range(col, len(matrix[0])):
                    submatrix = matrix[row:r + 1, col:c + 1]
                    if np.sum(submatrix) == 398:
                        result.append(submatrix)
    return result