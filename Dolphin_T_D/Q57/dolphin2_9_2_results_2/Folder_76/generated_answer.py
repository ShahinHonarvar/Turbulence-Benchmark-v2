import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for l in range(i, len(matrix)):
                for m in range(j, len(matrix[0])):
                    if sum(matrix[i:l + 1, j:m + 1]) == -255:
                        submatrices.append(matrix[i:l + 1, j:m + 1])
    return submatrices