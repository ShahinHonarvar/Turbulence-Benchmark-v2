import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for row in range(i + 1, len(matrix) + 1):
                for col in range(j + 1, len(matrix[0]) + 1):
                    submatrix = np.array(matrix[i:row, j:col]).flatten()
                    if np.sum(submatrix) == -157:
                        submatrices.append(submatrix.reshape(row - i, col - j))
    return submatrices