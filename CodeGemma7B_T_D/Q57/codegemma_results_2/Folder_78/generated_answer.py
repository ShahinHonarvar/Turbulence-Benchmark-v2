import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Returns the list of all submatrices of the given matrix with sum equal to 17.
    """
    rows, cols = matrix.shape
    submatrices = []
    for row1 in range(rows):
        for row2 in range(row1, rows):
            for col1 in range(cols):
                for col2 in range(col1, cols):
                    submatrix = matrix[row1:row2 + 1, col1:col2 + 1]
                    if submatrix.sum() == 17:
                        submatrices.append(submatrix)
    return submatrices