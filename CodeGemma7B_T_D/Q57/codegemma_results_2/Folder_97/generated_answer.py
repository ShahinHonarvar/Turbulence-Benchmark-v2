import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == -617:
                submatrix = matrix[i:i + 1, j:j + 1]
                if submatrix.sum() == -617:
                    result.append(submatrix)
    return result