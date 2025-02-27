import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix) - 2):
        for j in range(len(matrix[0]) - 2):
            if sum(matrix[i:i + 3, j:j + 3]) == 27:
                submatrices.append(matrix[i:i + 3, j:j + 3])
    return submatrices