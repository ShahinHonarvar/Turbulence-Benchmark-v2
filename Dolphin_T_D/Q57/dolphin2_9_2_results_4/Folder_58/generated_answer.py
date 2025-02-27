import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for x in range(i, matrix.shape[0]):
                for y in range(j, matrix.shape[1]):
                    if np.sum(matrix[i:x + 1, j:y + 1]) == -137:
                        submatrix = []
                        for row in matrix[i:x + 1]:
                            submatrix.append(row[j:y + 1])
                        submatrices.append(submatrix)
    return submatrices