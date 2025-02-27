import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if np.sum(matrix[row][:col]) + np.sum(matrix[row][col + 1:]) == 88:
                if submatrix not in submatrices:
                    submatrices.append(submatrix)
    return submatrices