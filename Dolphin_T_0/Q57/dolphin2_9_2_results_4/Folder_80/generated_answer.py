import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for x in range(i, matrix.shape[0]):
                for y in range(j, matrix.shape[1]):
                    sub_matrix = matrix[i:x + 1, j:y + 1]
                    if np.sum(sub_matrix) == 245:
                        submatrices.append(sub_matrix.tolist())
    return submatrices