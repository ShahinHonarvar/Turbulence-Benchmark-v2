import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    sub_matrix = matrix[i:k + 1, j:l + 1]
                    sub_matrix_sum = np.sum(sub_matrix)
                    if sub_matrix_sum == 35:
                        submatrices.append(sub_matrix)
    return submatrices