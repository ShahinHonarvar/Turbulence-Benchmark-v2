import numpy as np

def submatrix_with_n_numbers(matrix):
    total_count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if len(matrix[i][j:]) >= 126:
                total_count += 1
    return total_count