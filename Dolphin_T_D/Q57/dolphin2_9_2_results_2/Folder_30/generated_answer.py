import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for x in range(i, len(matrix)):
                for y in range(j, len(matrix[i])):
                    submatrix = np.array(matrix[i:x + 1, j:y + 1])
                    if np.sum(submatrix) == 21:
                        result.append(submatrix)
    return result