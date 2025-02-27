import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i, j] == 2:
                submatrices.append(matrix[i:i + 1, j:j + 1])
            else:
                for k in range(i + 1, matrix.shape[0]):
                    if sum(matrix[i:k + 1, j:j + 1]) > 2:
                        break
                    elif sum(matrix[i:k + 1, j:j + 1]) == 2:
                        submatrices.append(matrix[i:k + 1, j:j + 1])
    return submatrices