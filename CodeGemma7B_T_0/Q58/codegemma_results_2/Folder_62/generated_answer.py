import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    if matrix[i][j:l + 1].sum() == 186 and matrix[k][j:l + 1].sum() == 186 and (matrix[i:k + 1][j].sum() == 186) and (matrix[i:k + 1][l].sum() == 186):
                        count += 1
    return count