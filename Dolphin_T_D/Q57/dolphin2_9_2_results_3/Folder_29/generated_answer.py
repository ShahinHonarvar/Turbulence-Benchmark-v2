import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    height = len(matrix)
    width = len(matrix[0])
    for i in range(height):
        for j in range(width):
            for k in range(i, height):
                for l in range(j, width):
                    submatrix_sum = np.sum(matrix[i:k + 1, j:l + 1])
                    if submatrix_sum == 84:
                        submatrices.append(matrix[i:k + 1, j:l + 1])
    return submatrices