import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(i + 1, len(matrix)):
                for l in range(j + 1, len(matrix)):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == 100:
                        submatrices.append(submatrix)
    return submatrices