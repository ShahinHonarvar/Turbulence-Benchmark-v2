import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for size_i in range(i, len(matrix)):
                for size_j in range(j, len(matrix[i])):
                    submatrix = np.array(matrix[i:i + size_i + 1, j:j + size_j + 1])
                    if np.sum(submatrix) == -27:
                        result.append(submatrix)
    return result