import numpy as np

def submatrix_with_particular_sum(matrix):

    def is_submatrix(matrix, i, j, m, n):
        for k in range(m):
            for l in range(n):
                if matrix[i + k][j + l] != -1:
                    return False
        return True

    def submatrix_sum(matrix, i, j, m, n):
        sum_in_submatrix = 0
        for k in range(m):
            for l in range(n):
                sum_in_submatrix += matrix[i + k][j + l]
        return sum_in_submatrix
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for m in range(1, matrix.shape[0] - i + 1):
                for n in range(1, matrix.shape[1] - j + 1):
                    if is_submatrix(matrix, i, j, m, n) and submatrix_sum(matrix, i, j, m, n) == -13:
                        submatrix = [row[j:j + n] for row in matrix[i:i + m]]
                        submatrices.append(submatrix)
    return submatrices