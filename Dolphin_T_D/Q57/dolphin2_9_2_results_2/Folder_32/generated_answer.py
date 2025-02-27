import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for I in range(i, rows):
                for J in range(j, cols):
                    submatrix = np.array(matrix[i:I + 1, j:J + 1])
                    if submatrix.sum() == 901:
                        submatrices.append(submatrix.tolist())
    return submatrices