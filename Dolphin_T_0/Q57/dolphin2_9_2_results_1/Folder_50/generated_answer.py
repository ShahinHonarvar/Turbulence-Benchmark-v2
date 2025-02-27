import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for end_i in range(i, len(matrix)):
                for end_j in range(j, len(matrix[0])):
                    submatrix = np.array(matrix[i:end_i + 1, j:end_j + 1])
                    if np.sum(submatrix) == 95:
                        result.append(submatrix.tolist())
    return result