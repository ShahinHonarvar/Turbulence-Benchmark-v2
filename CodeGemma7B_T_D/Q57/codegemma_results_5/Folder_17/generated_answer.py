import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for x in range(len(matrix)):
        for y in range(len(matrix.T)):
            for w in range(x, len(matrix)):
                for h in range(y, len(matrix.T)):
                    submatrix = matrix[x:w + 1, y:h + 1]
                    if np.sum(submatrix) == 398:
                        result.append(submatrix)
    if not result:
        return []
    return result