from numpy import *

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            for k in range(len(matrix[0])):
                for l in range(k, len(matrix[0])):
                    submatrix = matrix[i:j + 1, k:l + 1]
                    if sum(submatrix.flatten()) == -97:
                        submatrices.append(submatrix)
    return submatrices