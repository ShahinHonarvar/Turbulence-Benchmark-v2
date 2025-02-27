import numpy as np

def submatrix_with_particular_sum(matrix):
    matrix = np.array(matrix)
    result_list = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    if np.sum(matrix[i:k + 1, j:l + 1]) == 95:
                        result_list.append(matrix[i:k + 1, j:l + 1])
    if not result_list:
        return []
    return result_list