import numpy as np

def submatrix_with_particular_sum(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            for m in range(len(matrix[0])):
                for n in range(m, len(matrix[0])):
                    submatrix = matrix[i:j + 1, m:n + 1]
                    if np.sum(submatrix) == -65:
                        return submatrix.tolist()
    return []