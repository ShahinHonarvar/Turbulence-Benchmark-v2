import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for ii in range(i + 1, rows):
                for jj in range(j + 1, cols):
                    submatrix_sum = np.sum(matrix[i:ii, j:jj])
                    if submatrix_sum == 830:
                        submatrices.append(matrix[i:ii, j:jj])
    return submatrices