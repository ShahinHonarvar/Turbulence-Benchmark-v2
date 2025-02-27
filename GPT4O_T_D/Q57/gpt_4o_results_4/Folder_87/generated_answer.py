import numpy as np

def submatrix_with_particular_sum(matrix):
    num_rows, num_cols = matrix.shape
    result = []
    for i in range(num_rows):
        for j in range(num_cols):
            for k in range(i, num_rows):
                for l in range(j, num_cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == 35:
                        result.append(submatrix)
    return result