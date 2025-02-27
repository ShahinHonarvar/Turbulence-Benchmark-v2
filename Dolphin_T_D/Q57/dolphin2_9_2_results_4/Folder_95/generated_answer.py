import numpy as np

def find_submatrix(matrix):
    result = []
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            for i in range(x, matrix.shape[0]):
                for j in range(y, matrix.shape[1]):
                    submatrix_sum = np.sum(matrix[x:i + 1, y:j + 1])
                    if submatrix_sum == 19:
                        result.append(matrix[x:i + 1, y:j + 1])
    return result