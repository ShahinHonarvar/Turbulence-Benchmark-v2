import numpy as np

def submatrix_with_particular_sum(matrix):
    approach = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for Z in range(i, len(matrix)):
                for W in range(j, len(matrix[i])):
                    if np.sum(matrix[i:Z + 1, j:W + 1]) == 394:
                        approach.append(matrix[i:Z + 1, j:W + 1])
    return approach