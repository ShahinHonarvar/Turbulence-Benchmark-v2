import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for x in range(i + 1, len(matrix)):
                for y in range(j + 1, len(matrix[0])):
                    sub = matrix[i:x + 1, j:y + 1]
                    if np.sum(sub) == 95:
                        submatrices.append(sub.tolist())
    return submatrices