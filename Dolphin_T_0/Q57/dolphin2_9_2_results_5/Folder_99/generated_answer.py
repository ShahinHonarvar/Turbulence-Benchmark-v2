import numpy as np

def submatrix_with_particular_sum(matrix):
    row, col = matrix.shape
    submatrices = []
    for r1 in range(row + 1):
        for c1 in range(col + 1):
            for r2 in range(r1, row + 1):
                for c2 in range(c1, col + 1):
                    submatrix_sum = np.sum(matrix[r1:r2, c1:c2])
                    if submatrix_sum == -185:
                        submatrix = matrix[r1:r2, c1:c2]
                        submatrices.append(submatrix.tolist())
    return submatrices