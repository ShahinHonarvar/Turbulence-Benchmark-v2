import numpy as np

def submatrix_with_particular_sum(matrix):
    sub_matrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for x in range(i + 1, len(matrix) + 1):
                for y in range(j + 1, len(matrix[0]) + 1):
                    sub_matrix = matrix[i:x, j:y]
                    if np.sum(sub_matrix) == 2:
                        sub_matrices.append(sub_matrix.tolist())
    return sub_matrices