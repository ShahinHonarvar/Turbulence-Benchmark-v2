import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            for x in range(i + 1, len(matrix)):
                for y in range(j + 1, len(matrix[0])):
                    submatrix_sum = np.sum(matrix[i:x + 1, j:y + 1])
                    if submatrix_sum == 394:
                        submatrices.append(matrix[i:x + 1, j:y + 1])
    return submatrices