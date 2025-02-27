import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for x in range(i, len(matrix)):
                for y in range(j, len(matrix[0])):
                    if np.sum(matrix[i:x + 1, j:y + 1]) == 84:
                        result.append(matrix[i:x + 1, j:y + 1])
    return result