import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for row in range(i + 1, len(matrix) + 1):
                for col in range(j + 1, len(matrix[0]) + 1):
                    if np.sum(matrix[i:row, j:col]) == 95:
                        result.append(matrix[i:row, j:col].tolist())
    return result