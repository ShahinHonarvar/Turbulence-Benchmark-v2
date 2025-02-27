import numpy as np

def submatrix_with_particular_sum(matrix):
    """
            returns list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 0. If no such submatrix is found, the function should return an empty list
            """
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows):
                for l in range(j + 1, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == 0:
                        submatrices.append(submatrix)
    return submatrices