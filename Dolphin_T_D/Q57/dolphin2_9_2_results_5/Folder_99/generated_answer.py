import numpy as np

def submatrix_with_particular_sum(matrix):
    sub_matrices = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    tmp = np.sum(matrix[i:k + 1, j:l + 1])
                    if tmp == -185:
                        sub_matrices.append(matrix[i:k + 1, j:l + 1].tolist())
    return sub_matrices