import numpy as np

def submatrix_with_particular_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for i in range(rows):
        for j in range(cols):
            for end_row in range(i, rows):
                for end_col in range(j, cols):
                    submatrix = matrix[i:end_row + 1, j:end_col + 1]
                    if np.sum(submatrix) == -13:
                        result.append(submatrix.tolist())
    return result