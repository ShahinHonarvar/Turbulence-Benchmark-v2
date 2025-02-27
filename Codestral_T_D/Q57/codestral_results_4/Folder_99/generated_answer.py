import numpy as np
import itertools

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for rows in range(1, matrix.shape[0] + 1):
        for cols in range(1, matrix.shape[1] + 1):
            for i in range(matrix.shape[0] - rows + 1):
                for j in range(matrix.shape[1] - cols + 1):
                    submatrix = matrix[i:i + rows, j:j + cols]
                    if np.sum(submatrix) == -185:
                        submatrices.append(submatrix)
    return submatrices