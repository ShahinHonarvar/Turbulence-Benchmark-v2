import numpy as np

def submatrix_with_particular_sum(matrix):
    size = len(matrix)
    submatrices = []
    for i in range(size):
        for j in range(size):
            for x in range(i + 1, size + 1):
                for y in range(j + 1, size + 1):
                    sub_matrix = matrix[i:x, j:y]
                    if np.sum(sub_matrix) == -4:
                        submatrices.append(sub_matrix.tolist())
    return submatrices