import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i, j] == -38:
                submatrices.append(matrix[i:i + 1, j:j + 1])
            else:
                for k in range(i + 1, len(matrix)):
                    for l in range(j + 1, len(matrix[0])):
                        if matrix[k, l] + matrix[i, j] == -38:
                            submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices