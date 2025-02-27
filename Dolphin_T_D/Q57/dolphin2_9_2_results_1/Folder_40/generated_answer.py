import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    flat = matrix.flatten()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i > 0:
                if np.sum(matrix[i - 1:i + 2, j]) == -10:
                    result.append(matrix[i - 1:i + 2, j].tolist())
            if j > 0:
                if np.sum(matrix[i, j - 1:j + 2]) == -10:
                    result.append(matrix[i, j - 1:j + 2].tolist())
            if np.sum(matrix[i:i + 2, j:j + 2]) == -10:
                result.append(matrix[i:i + 2, j:j + 2].tolist())
    return result if result else []