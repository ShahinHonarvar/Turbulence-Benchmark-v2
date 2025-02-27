import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for x in range(i, rows):
                for y in range(j, cols):
                    current_sum = np.sum(matrix[i:x + 1, j:y + 1])
                    if current_sum == -59:
                        submatrices.append(matrix[i:x + 1, j:y + 1])
    return submatrices