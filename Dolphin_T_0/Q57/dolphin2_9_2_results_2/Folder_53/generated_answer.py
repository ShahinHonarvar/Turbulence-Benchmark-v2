import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i + 2 < len(matrix) and j + 2 < len(matrix[0]):
                sub_matrix = matrix[i:i + 3, j:j + 3]
                if np.sum(sub_matrix) == -37:
                    submatrices.append(sub_matrix)
    return submatrices