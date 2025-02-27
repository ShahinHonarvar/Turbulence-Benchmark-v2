import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for r1 in range(len(matrix)):
        for r2 in range(r1 + 1, len(matrix) + 1):
            for c1 in range(len(matrix[0])):
                for c2 in range(c1 + 1, len(matrix[0]) + 1):
                    submatrix = matrix[r1:r2, c1:c2]
                    if submatrix.sum() == -25:
                        result.append(submatrix)
    return result