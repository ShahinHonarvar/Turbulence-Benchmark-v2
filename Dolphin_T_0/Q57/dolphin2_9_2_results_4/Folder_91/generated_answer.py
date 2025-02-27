import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    num_rows, num_cols = matrix.shape
    for i in range(num_rows):
        for j in range(num_cols):
            for x in range(i, num_rows):
                for y in range(j, num_cols):
                    submatrix = matrix[i:x + 1, j:y + 1]
                    if sum(submatrix.flatten()) == -6:
                        result.append(submatrix.tolist())
    return result