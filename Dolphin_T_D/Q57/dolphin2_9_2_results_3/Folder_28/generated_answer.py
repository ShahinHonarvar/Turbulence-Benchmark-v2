import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    size = matrix.shape[0]
    for i in range(size):
        for j in range(size):
            for m in range(i, size):
                for n in range(j, size):
                    submatrix = matrix[i:m + 1, j:n + 1]
                    if np.sum(submatrix) == 15:
                        result.append(submatrix)
    if result:
        return result
    else:
        return []