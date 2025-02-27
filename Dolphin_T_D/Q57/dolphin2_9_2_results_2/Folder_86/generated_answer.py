import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for h in range(i, len(matrix)):
                for w in range(j, len(matrix[0])):
                    submatrix = matrix[i:h + 1, j:w + 1]
                    if np.sum(submatrix) == -394:
                        submatrices.append(submatrix)
    return submatrices