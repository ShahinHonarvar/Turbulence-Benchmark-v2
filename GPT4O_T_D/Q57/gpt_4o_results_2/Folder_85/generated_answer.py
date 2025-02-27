import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(top, left, bottom, right):
        total = 0
        for i in range(top, bottom + 1):
            for j in range(left, right + 1):
                total += matrix[i][j]
        return total
    rows, cols = matrix.shape
    submatrices = []
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    if submatrix_sum(top, left, bottom, right) == -87:
                        submatrix = matrix[top:bottom + 1, left:right + 1]
                        submatrices.append(submatrix.tolist())
    return submatrices