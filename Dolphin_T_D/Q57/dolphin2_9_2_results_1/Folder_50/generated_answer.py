import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, columns = matrix.shape
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(columns):
                for c2 in range(c1, columns):
                    submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                    if np.sum(submatrix) == 95:
                        submatrices.append(submatrix.tolist())
    return submatrices