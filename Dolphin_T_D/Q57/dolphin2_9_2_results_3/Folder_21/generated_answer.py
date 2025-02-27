import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for row1 in range(i, matrix.shape[0]):
                for col1 in range(j, matrix.shape[1]):
                    for row2 in range(i, row1 + 1):
                        for col2 in range(j, col1 + 1):
                            if np.sum(matrix[row2:row1 + 1, col2:col1 + 1]) == -936:
                                submatrices.append(matrix[row2:row1 + 1, col2:col1 + 1])
    return submatrices