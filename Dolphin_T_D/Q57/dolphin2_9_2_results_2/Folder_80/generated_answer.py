import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, columns = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(columns):
            for x in range(i, rows):
                for y in range(j, columns):
                    sub = np.sum(matrix[i:x + 1, j:y + 1])
                    if sub == 245:
                        submatrices.append(matrix[i:x + 1, j:y + 1].tolist())
    return submatrices