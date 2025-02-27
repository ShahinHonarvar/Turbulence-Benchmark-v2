import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for row in range(len(matrix)):
                for col in range(len(matrix[0])):
                    submatrix_sum = sum(sum(matrix[row:row + i + 1, col:col + j + 1]))
                    if submatrix_sum == -93:
                        submatrices.append(matrix[row:row + i + 1, col:col + j + 1])
    return submatrices