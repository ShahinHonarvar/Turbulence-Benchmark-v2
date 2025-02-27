import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 118:
                if i - 1 >= 0 and j - 1 >= 0:
                    if matrix[i - 1][j] == 118 and matrix[i][j - 1] == 118 and (matrix[i - 1][j - 1] == 118):
                        count += 1
                elif matrix[i][j] == 118:
                    count += 1
    return count