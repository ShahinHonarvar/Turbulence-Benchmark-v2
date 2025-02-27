import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, columns = matrix.shape
    result = []
    for i in range(rows):
        for j in range(columns):
            for k in range(i, rows):
                for l in range(j, columns):
                    sub_matrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(sub_matrix) == 66:
                        result.append(sub_matrix)
    return result