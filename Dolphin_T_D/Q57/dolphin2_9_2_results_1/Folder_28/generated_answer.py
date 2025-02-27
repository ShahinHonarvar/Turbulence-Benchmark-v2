import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix) - 3):
        for j in range(len(matrix[0]) - 4):
            submatrix = matrix[i:i + 4, j:j + 5]
            if np.sum(submatrix) == 15:
                submatrices.append(submatrix)
    return submatrices