import numpy as np

def submatrix_with_particular_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for m in range(i, rows):
                for n in range(j, cols):
                    submatrix = matrix[i:m + 1, j:n + 1]
                    if np.sum(submatrix) == -44:
                        submatrices.append(submatrix.tolist())
    return submatrices