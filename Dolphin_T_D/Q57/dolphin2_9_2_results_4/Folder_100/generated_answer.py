import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for n in range(i + 1, len(matrix) + 1):
                for m in range(j + 1, len(matrix[0]) + 1):
                    submatrix_sum = np.sum(matrix[i:n, j:m])
                    if submatrix_sum == 28:
                        submatrices.append(matrix[i:n, j:m])
    return submatrices