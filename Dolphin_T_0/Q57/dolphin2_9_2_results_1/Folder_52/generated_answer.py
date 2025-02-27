import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for x in range(i + 1, len(matrix) + 1):
                for y in range(j + 1, len(matrix[0]) + 1):
                    submatrix = np.array(matrix[i:x, j:y])
                    if np.sum(submatrix) == 100:
                        submatrices.append(submatrix.tolist())
    return submatrices