import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            for h in range(x + 1, len(matrix) + 1):
                for w in range(y + 1, len(matrix) + 1):
                    submatrix = matrix[x:h, y:w]
                    if int(np.sum(submatrix)) == 416:
                        submatrices.append(submatrix)
    return submatrices