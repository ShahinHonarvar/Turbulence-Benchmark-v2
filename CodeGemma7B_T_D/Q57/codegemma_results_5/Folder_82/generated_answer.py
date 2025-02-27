import numpy as np

def submatrix_with_particular_sum(matrix):
    for r in range(matrix.shape[0]):
        for c in range(matrix.shape[1]):
            if matrix[r, c] == -27:
                submatrix = []
                for i in range(r, matrix.shape[0]):
                    for j in range(c, matrix.shape[1]):
                        submatrix.append(matrix[i, j])
                if sum(submatrix) == -27:
                    return submatrix
    return []