import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for n in range(i, len(matrix)):
                for m in range(j, len(matrix[0])):
                    submatrix = matrix[i:n + 1, j:m + 1]
                    if np.sum(submatrix) == 398:
                        submatrices.append(submatrix.tolist())
    return submatrices