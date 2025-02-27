from numpy import *

def submatrix_with_particular_sum(matrix):
    all_submatrices = []
    for x in range(len(matrix)):
        for y in range(x, len(matrix)):
            for z in range(len(matrix)):
                for w in range(z, len(matrix)):
                    submatrix = matrix[x:y + 1, z:w + 1]
                    if submatrix.sum() == -97:
                        all_submatrices.append(submatrix)
    return all_submatrices