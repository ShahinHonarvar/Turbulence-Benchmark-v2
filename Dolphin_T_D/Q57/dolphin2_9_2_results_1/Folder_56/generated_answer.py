import numpy as np

def submatrix_with_particular_sum(matrix):
    sub_matrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for size_i in range(1, len(matrix) - i + 1):
                for size_j in range(1, len(matrix[0]) - j + 1):
                    sub_matrix = np.array(matrix[i:i + size_i, j:j + size_j])
                    if np.sum(sub_matrix) == -50:
                        sub_matrices.append(sub_matrix.tolist())
    return sub_matrices