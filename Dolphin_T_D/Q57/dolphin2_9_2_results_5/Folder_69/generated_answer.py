import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    sum_matrix = np.sum(matrix, axis=0)
    for i in range(matrix.shape[1]):
        for j in range(i + 1, matrix.shape[1]):
            if sum_matrix[i] - sum_matrix[j] == 752:
                current_result = matrix[:, i:j]
                result.append(current_result)
    return result