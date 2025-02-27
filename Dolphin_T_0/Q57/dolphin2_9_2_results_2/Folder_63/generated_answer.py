import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrix_list = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, cols + 1):
                    if np.sum(matrix[i:k, j:l]) == 64:
                        submatrix_list.append(matrix[i:k, j:l])
    return submatrix_list