import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sum(matrix, top, left, bottom, right):
        sub_sum = 0
        for i in range(top, bottom + 1):
            for j in range(left, right + 1):
                sub_sum += matrix[i][j]
        return sub_sum
    rows, cols = matrix.shape
    result = []
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    if get_submatrix_sum(matrix, top, left, bottom, right) == -394:
                        submatrix = matrix[top:bottom + 1, left:right + 1]
                        result.append(submatrix.tolist())
    return result