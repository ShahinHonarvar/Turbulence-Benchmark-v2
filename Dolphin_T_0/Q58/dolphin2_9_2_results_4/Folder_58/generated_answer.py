import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 185:
                submatrix_count += 1
    return submatrix_count if submatrix_count > 0 else 0