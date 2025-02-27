import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    matrix_size = matrix.shape
    for i in range(matrix_size[0]):
        for j in range(matrix_size[1]):
            for x in range(i, matrix_size[0]):
                for y in range(j, matrix_size[1]):
                    submatrix = matrix[i:x + 1, j:y + 1]
                    if np.sum(submatrix) == -811:
                        submatrices.append(submatrix)
    return submatrices if len(submatrices) > 0 else []