import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for row in range(i, rows):
                for col in range(j, cols):
                    submatrix_sum = np.sum(matrix[i:row + 1, j:col + 1])
                    if submatrix_sum == 80:
                        result.append(matrix[i:row + 1, j:col + 1])
    return result