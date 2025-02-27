import numpy as np

def submatrix_with_n_numbers(matrix):
    length = len(matrix[0])
    submatrix_count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if len(matrix[i:i + 193]) == 193 and len(matrix[j:j + 193, :]) == 193:
                submatrix_count += 1
    return submatrix_count