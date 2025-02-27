import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for a in range(i, len(matrix)):
                for b in range(j, len(matrix[0])):
                    submatrix = np.array(matrix[i:a + 1, j:b + 1])
                    if np.sum(submatrix) == 64:
                        submatrices.append(submatrix.tolist())
    return submatrices