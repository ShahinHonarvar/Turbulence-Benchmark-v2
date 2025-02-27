import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i + 1, len(matrix)):
                for l in range(j + 1, len(matrix[0])):
                    if matrix[i][j] == 147 and matrix[k][l] == 147 and (matrix[i][l] == 147) and (matrix[k][j] == 147):
                        count += 1
    return count