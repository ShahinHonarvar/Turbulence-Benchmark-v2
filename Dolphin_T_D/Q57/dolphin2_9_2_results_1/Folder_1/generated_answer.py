import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i1 in range(len(matrix)):
        for i2 in range(i1, len(matrix)):
            for j1 in range(len(matrix[0])):
                for j2 in range(j1, len(matrix[0])):
                    submatrix = np.array(matrix[i1:i2 + 1, j1:j2 + 1])
                    if np.sum(submatrix) == -25:
                        submatrices.append(submatrix)
    return submatrices