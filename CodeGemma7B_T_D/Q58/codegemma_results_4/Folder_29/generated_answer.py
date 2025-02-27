import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i + 1, len(matrix)):
                for l in range(j + 1, len(matrix[0])):
                    if matrix[i][j] == 19 and matrix[k][l] == 19 and (sorted(matrix[i][j:l + 1]) == list(range(j, l + 2))):
                        submatrix_count += 1
    return submatrix_count