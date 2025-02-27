import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for x in range(i, len(matrix)):
                for y in range(j, len(matrix[0])):
                    if sum(matrix[i:x + 1, j:y + 1]) == -47:
                        m = matrix[i:x + 1, j:y + 1]
                        result.append(m.tolist())
    return result