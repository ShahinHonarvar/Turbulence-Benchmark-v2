import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for row in range(i, rows):
                for col in range(j, cols):
                    sub_matrix = matrix[i:row + 1, j:col + 1]
                    if np.sum(sub_matrix) == 38:
                        submatrices.append(sub_matrix)
    return submatrices