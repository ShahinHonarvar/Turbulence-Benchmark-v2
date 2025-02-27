import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for x in range(i, len(matrix)):
                for y in range(j, len(matrix[0])):
                    submatrix = np.array(matrix[i:x + 1, j:y + 1]).flatten()
                    if sum(submatrix) == -37:
                        result.append(submatrix)
    return result