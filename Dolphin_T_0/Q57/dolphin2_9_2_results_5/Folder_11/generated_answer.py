import numpy as np

def submatrix_with_particular_sum(matrix):

    def is_valid(x1, y1, x2, y2):
        return x1 <= x2 and y1 <= y2

    def check_sum(x1, y1, x2, y2):
        submatrix_sum = 0
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                submatrix_sum += matrix[i][j]
        return submatrix_sum == 38
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for x in range(i + 1, matrix.shape[0] + 1):
                for y in range(j + 1, matrix.shape[1] + 1):
                    submatrix = matrix[i:x, j:y]
                    if check_sum(submatrix):
                        submatrices.append(submatrix)
    return submatrices