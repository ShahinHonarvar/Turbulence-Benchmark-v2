import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for i_end in range(i, rows):
                for j_end in range(j, cols):
                    submatrix = matrix[i:i_end + 1, j:j_end + 1]
                    if np.sum(submatrix) == 87:
                        result.append(submatrix)
    return result