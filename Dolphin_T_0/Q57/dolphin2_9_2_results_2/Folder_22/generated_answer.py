import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    sub_sum = np.sum(matrix[i:k + 1, j:l + 1])
                    if sub_sum == -38:
                        result = matrix[i:k + 1, j:l + 1]
                        submatrices.append(result)
    if not submatrices:
        return []
    else:
        return submatrices