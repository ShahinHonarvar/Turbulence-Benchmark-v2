import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.flatten().tolist().count(69) == 69:
                        count += 1
                    elif matrix[i][j] == 69 and matrix[k][l] == 69:
                        count += 1
    return count