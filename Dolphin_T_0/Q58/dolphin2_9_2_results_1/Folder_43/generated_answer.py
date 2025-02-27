import numpy as np

def submatrix_with_n_numbers(matrix):
    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 85:
                for k in range(i, len(matrix)):
                    for l in range(j, len(matrix[0])):
                        submatrix = matrix[i:k + 1, j:l + 1]
                        if len(submatrix) * len(submatrix[0]) == 85:
                            result += 1
    return result