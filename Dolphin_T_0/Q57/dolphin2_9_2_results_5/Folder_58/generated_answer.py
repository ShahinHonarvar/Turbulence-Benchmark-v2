import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            sum = 0
            for x in range(i, matrix.shape[0]):
                for y in range(j, matrix.shape[1]):
                    sum += matrix[x, y]
                    if sum == -137:
                        submatrix = matrix[i:x + 1, j:y + 1]
                        submatrices.append(submatrix.tolist())
    return submatrices