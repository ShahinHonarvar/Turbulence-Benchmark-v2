import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(j + 1, len(matrix[0])):
                for l in range(i + 1, len(matrix)):
                    if (matrix[l][k] and matrix[l][j] and matrix[i][k] and matrix[i][j]).all():
                        count += 1
    return count